from PIL import Image
import os
import time
from utils import *
import ai

ai.init()

def read_image():
	# if your OS is win
    os.system("../../dependency/platform-tools-windows/adb.exe shell screencap -p /sdcard/autojump.png")
    os.system("../../dependency/platform-tools-windows/adb.exe pull /sdcard/autojump.png .")
	## if your OS is mac 
	# os.system("../../dependency/platform-tools-macos/adb shell screencap -p /sdcard/autojump.png")
	# os.system("../../dependency/platform-tools-macos/adb pull /sdcard/autojump.png .")
    im = Image.open("autojump.png")
    return im


def click_screen(press_time):
	# if your OS is win 
    os.system("../../dependency/platform-tools-windows/adb.exe shell input swipe 50 50 50 50 " + str(int(press_time)))
	## is your OS is mac 
	# os.system("../../dependency/platform-tools-macos/adb shell input swipe 50 50 50 50 " + str(int(press_time)))

def jumper():

    #ai.init()
    # print(screenShot)
	distance = 0.0
	screenShot = Image.open('./autojump.png')

    # ******************
    # start your code here
	piece_x, piece_y, board_x, board_y = find_piece_and_board(im)
	distance = math.sqrt((board_x - piece_x) ** 2 + (board_y - piece_y) ** 2)
	return distance
	# ******************


if __name__ == '__main__':
    jumper()

