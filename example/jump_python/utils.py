#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
author: Zhou Xiangxin
time: 2018/6/3

"""
import sys
from PIL import Image
import matplotlib.pyplot as plt
import math
import ai
import time
import os
import random
import re

# hyper-parameters
wc_top = 0
wc_left = 0
wc_width = 1080
wc_height = 1920

piece_base_height_1_2 = 50
piece_body_width = 50
press_coefficient = 1.392


def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v


def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def find_piece_and_board(im):
    w, h = im.size

    piece_x_sum = 0
    piece_x_c = 0
    piece_y_max = 0
    board_x = 0
    board_y = 0

    left_value = 0
    left_count = 0
    right_value = 0
    right_count = 0
    from_left_find_board_y = 0
    from_right_find_board_y = 0

    scan_x_border = int(w / 8)  # 扫描棋子时的左右边界
    scan_start_y = 0  # 扫描的起始y坐标
    im_pixel = im.load()
    # 以50px步长，尝试探测scan_start_y
    for i in range(int(h / 3), int(h * 2 / 3), 50):
        last_pixel = im_pixel[0, i]
        for j in range(1, w):
            pixel = im_pixel[j, i]
            # 不是纯色的线，则记录scan_start_y的值，准备跳出循环
            if pixel[0] != last_pixel[0] or pixel[1] != last_pixel[1] or pixel[2] != last_pixel[2]:
                scan_start_y = i - 50
                break
        if scan_start_y:
            break
    # print('scan_start_y: ', scan_start_y)

    # 从scan_start_y开始往下扫描，棋子应位于屏幕上半部分，这里暂定不超过2/3
    for i in range(scan_start_y, int(h * 2 / 3)):
        for j in range(scan_x_border, w - scan_x_border):  # 横坐标方面也减少了一部分扫描开销
            pixel = im_pixel[j, i]
            # 根据棋子的最低行的颜色判断，找最后一行那些点的平均值，这个颜色这样应该 OK，暂时不提出来
            if (50 < pixel[0] < 60) and (53 < pixel[1] < 63) and (95 < pixel[2] < 110):
                piece_x_sum += j
                piece_x_c += 1
                piece_y_max = max(i, piece_y_max)

    if not all((piece_x_sum, piece_x_c)):
        return 0, 0, 0, 0
    piece_x = piece_x_sum / piece_x_c
    piece_y = piece_y_max - piece_base_height_1_2  # 上移棋子底盘高度的一半

    for i in range(int(h / 3), int(h * 2 / 3)):

        last_pixel = im_pixel[0, i]
        # 计算阴影的RGB值,通过photoshop观察,阴影部分其实就是背景色的明度V 乘以0.7的样子
        h, s, v = rgb2hsv(last_pixel[0], last_pixel[1], last_pixel[2])
        r, g, b = hsv2rgb(h, s, v * 0.7)

        if from_left_find_board_y and from_right_find_board_y:
            break

        if not board_x:
            board_x_sum = 0
            board_x_c = 0

            for j in range(w):
                pixel = im_pixel[j, i]
                # 修掉脑袋比下一个小格子还高的情况的 bug
                if abs(j - piece_x) < piece_body_width:
                    continue

                # 修掉圆顶的时候一条线导致的小 bug，这个颜色判断应该 OK，暂时不提出来
                if abs(pixel[0] - last_pixel[0]) + abs(pixel[1] - last_pixel[1]) + abs(pixel[2] - last_pixel[2]) > 10:
                    board_x_sum += j
                    board_x_c += 1
            if board_x_sum:
                board_x = board_x_sum / board_x_c
        else:
            # 继续往下查找,从左到右扫描,找到第一个与背景颜色不同的像素点,记录位置
            # 当有连续3个相同的记录时,表示发现了一条直线
            # 这条直线即为目标board的左边缘
            # 然后当前的 y 值减 3 获得左边缘的第一个像素
            # 就是顶部的左边顶点
            for j in range(w):
                pixel = im_pixel[j, i]
                # 修掉脑袋比下一个小格子还高的情况的 bug
                if abs(j - piece_x) < piece_body_width:
                    continue
                if (abs(pixel[0] - last_pixel[0]) + abs(pixel[1] - last_pixel[1]) + abs(pixel[2] - last_pixel[2])
                        > 10) and (abs(pixel[0] - r) + abs(pixel[1] - g) + abs(pixel[2] - b) > 10):
                    if left_value == j:
                        left_count = left_count + 1
                    else:
                        left_value = j
                        left_count = 1

                    if left_count > 3:
                        from_left_find_board_y = i - 3
                    break
            # 逻辑跟上面类似,但是方向从右向左
            # 当有遮挡时,只会有一边有遮挡
            # 算出来两个必然有一个是对的
            for j in range(w)[::-1]:
                pixel = im_pixel[j, i]
                # 修掉脑袋比下一个小格子还高的情况的 bug
                if abs(j - piece_x) < piece_body_width:
                    continue
                if (abs(pixel[0] - last_pixel[0]) + abs(pixel[1] - last_pixel[1]) + abs(pixel[2] - last_pixel[2])
                        > 10) and (abs(pixel[0] - r) + abs(pixel[1] - g) + abs(pixel[2] - b) > 10):
                    if right_value == j:
                        right_count = left_count + 1
                    else:
                        right_value = j
                        right_count = 1

                    if right_count > 3:
                        from_right_find_board_y = i - 3
                    break

    # 如果顶部像素比较多,说明图案近圆形,相应的求出来的值需要增大,这里暂定增大顶部宽的三分之一
    if board_x_c > 5:
        from_left_find_board_y = from_left_find_board_y + board_x_c / 3
        from_right_find_board_y = from_right_find_board_y + board_x_c / 3

    # 按实际的角度来算，找到接近下一个 board 中心的坐标 这里的角度应该是30°,值应该是tan 30°,math.sqrt(3) / 3
    board_y = piece_y - abs(board_x - piece_x) * math.sqrt(3) / 3

    # 从左从右取出两个数据进行对比,选出来更接近原来老算法的那个值
    if abs(board_y - from_left_find_board_y) > abs(from_right_find_board_y):
        new_board_y = from_right_find_board_y
    else:
        new_board_y = from_left_find_board_y

    if not all((board_x, board_y)):
        return 0, 0, 0, 0

    return piece_x, piece_y, board_x, new_board_y


def jump(distance):
    '''
    跳跃一定的距离
    '''
    if ai.get_result_len() >= 10:  # 需采集10条样本以上
        k, b, v = ai.computing_k_b_v(distance)
        press_time = distance * k[0] + b
        # print('Y = {k} * X + {b}'.format(k=k[0], b=b))

    else:
        press_time = distance * press_coefficient
        press_time = max(press_time, 200)  # 设置 200ms 是最小的按压时间

    # press_time = int(press_time)
    # press_time = press_time / 1000.
    # pyautogui.mouseDown()
    # time.sleep(press_time)
    # pyautogui.mouseUp()
    return press_time
