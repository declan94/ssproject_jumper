import sys
import os
import subprocess
import time
import cv2
import check_result.check_result as check


if len(sys.argv) != 2:
    print("Insufficient arguments. Exiting...")
    exit()

platform = sys.platform
if platform != "win32" and platform != "darwin":
    print("Unsupported platform. Exiting...")
    exit()

lang = sys.argv[1].lower()
if lang != "python" and lang != "cpp" and lang != "matlab":
    print("Unsupported language. Exiting...")
    exit()

if lang == "matlab":
    if not os.path.isfile('./jump_matlab/jumper.m'):
        print('Source code does not exist! Exiting...')
        exit()
    import matlab.engine
    engine = matlab.engine.start_matlab()
elif lang == "python":
    if not os.path.isfile('./jump_python/jumper.py'):
        print('Source code does not exist! Exiting...')
        exit()
    import jump_python.jumper as jumper
else:
    if platform == "win32":
        if not os.path.isfile('./jump_cpp/jumper.exe'):
            print('Executable file does not exist! Exiting...')
            exit()
    if platform == "darwin":
        if not os.path.isfile('./jump_cpp/jumper'):
            print('Executable file does not exist! Exiting...')
            exit()


def get_screenshot():
    if platform == "win32":
        os.system(
            'cd ../dependency/platform-tools-windows/ && adb.exe shell screencap -p /sdcard/autojump.png')
        os.system(
            'cd ../dependency/platform-tools-windows/ && adb.exe pull /sdcard/autojump.png ../../test/')
    else:
        os.system(
            'cd ../dependency/platform-tools-macos/ && ./adb shell screencap -p /sdcard/autojump.png')
        os.system(
            'cd ../dependency/platform-tools-macos/ && ./adb pull /sdcard/autojump.png ../../test/')


def press_screen(press_time):
    if platform == "win32":
        os.system(
            'cd ../dependency/platform-tools-windows/ && adb.exe shell input swipe 500 1600 500 1602 ' + str(press_time))
    else:
        os.system(
            'cd ../dependency/platform-tools-macos/ && ./adb shell input swipe 500 1600 500 1602 ' + str(press_time))


def restart(pos):
    if platform == "win32":
        os.system(
            'cd ../dependency/platform-tools-windows/ && adb.exe shell input tap '+str(pos[0])+' '+str(pos[1]))
    else:
        os.system(
            'cd ../dependency/platform-tools-macos/ && ./adb shell input tap ' + str(pos[0]) + ' ' + str(pos[1]))


while True:
    get_screenshot()
    screenshot = cv2.imread('./autojump.png')

    score, restart_pos = check.check_result(screenshot)
    if score >= 0:
        with open("./result.txt", 'a') as f:
            f.write("score: ", score)
            f.write("\n")
        restart(restart_pos)

    press_time = 0
    if lang == "python":
        press_time = jumper.jumper()
    elif lang == "cpp":
        if platform == "win32":
            press_time = subprocess.getoutput('cd jump_cpp && jumper.exe')
        if platform == "darwin":
            press_time = subprocess.getoutput('cd jump_cpp && ./jumper')
    else:
        engine.addpath("./jump_matlab")
        press_time = engine.jumper()

    print('Press time: ' + str(press_time))
    press_screen(press_time)

    time.sleep(2)
