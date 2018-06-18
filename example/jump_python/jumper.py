from PIL import Image
import os
import time
from utils import *
import ai

ai.init()


def read_image():
    # if your OS is win
    os.system(
        "cd ../../dependency/platform-tools-windows && adb.exe shell screencap -p /sdcard/autojump.png")
    os.system("cd ../../dependency/platform-tools-windows && adb.exe pull /sdcard/autojump.png ../../src/jump_python")
    # if your OS is mac
    # os.system("cd ../../dependency/platform-tools-macos && ./adb shell screencap -p /sdcard/autojump.png")
    # os.system("cd ../../dependency/platform-tools-macos && ./adb pull /sdcard/autojump.png ../../src/jump_python")
    im = Image.open("autojump.png")
    return im


def click_screen(press_time):
    # if your OS is win
    os.system("cd ../../dependency/platform-tools-windows && adb.exe shell input swipe 50 50 50 50 " + str(int(press_time)))
    # is your OS is mac
    # os.system("cd ../../dependency/platform-tools-macos && ./adb shell input swipe 50 50 50 50  "+str(int(press_time)))


def jumper():

    # ai.init()
    # print(screenShot)
    distance = 0.0
    screenShot = Image.open('./autojump.png')

    # ******************
    # start your code here
    piece_x, piece_y, board_x, board_y = find_piece_and_board(screenShot)
    distance = math.sqrt((board_x - piece_x) ** 2 + (board_y - piece_y) ** 2)
    return distance
    # ******************


if __name__ == '__main__':
    jumper()
