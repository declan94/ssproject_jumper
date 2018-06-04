import os

time_coeff = 1.392


def get_screenshot():
    # Change 'adb.exe' to 'adb' on macOS
    os.system('../dependency/adb.exe shell screencap -p /sdcard/autojump.png')
    os.system('../dependency/adb.exe pull /sdcard/autojump.png .')


def press_screen(distance):
    # Change 'adb.exe' to 'adb' on macOS
    press_time = int(distance * time_coeff / 1000)
    system('../dependency/adb.exe shell input swipe 500 1600 500 1602 ' + str(press_time))


def main():
    # Code here
    pass
