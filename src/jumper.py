import os

time_coeff = 1.392


def get_screenshot():
    # Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to 'adb' on macOS; you may need to use `chmod +X /dependency/platform-tools-macos/adb` first
    os.system(
        '../dependency/platform-tools-windows/adb.exe shell screencap -p /sdcard/autojump.png')
    os.system(
        '../dependency/platform-tools-windows/adb.exe pull /sdcard/autojump.png .')


def press_screen(distance):
    # Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to 'adb' on macOS; you may need to use `chmod +X /dependency/platform-tools-macos/adb` first
    press_time = int(distance * time_coeff / 1000)
    system('../dependency/platform-tools-windows/adb.exe shell input swipe 500 1600 500 1602 ' + str(press_time))


def main():
    # Code here
    pass
