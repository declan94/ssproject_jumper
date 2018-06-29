import sys
import os
import matlab.engine
import check_result.check_result as check
import cv2

# print(sys.argv)
mType = sys.argv[1]
dis = 0.0  # 学生返回的距离

if mType == '2' or mType == '5':
    eng = matlab.engine.start_matlab()

while True:
    if mType == '0' or mType == '1' or mType == '2':
        os.system(
            "cd ../dependency/platform-tools-windows && adb.exe shell screencap -p /sdcard/autojump.png")
        os.system(
            "cd ../dependency/platform-tools-windows && adb.exe pull /sdcard/autojump.png ../../test")
    else:
        os.system(
            "cd ../dependency/platform-tools-macos && ./adb shell screencap -p /sdcard/autojump.png")
        os.system(
            "cd ../dependency/platform-tools-macos && ./adb pull /sdcard/autojump.png ../../test")
    img = cv2.imread("./autojump.png")
    score, pos = check.check_result(img)
    if score >= 0:
        with open("./result.txt", 'a') as f:
            f.write("score:", score)
            f.write("\n")
        if mType == '0' or mType == '1' or mType == '2':
            os.system("cd ../dependency/platform-tools-windows && adb.exe shell input tap " +
                      str(pos[0])+' '+str(pos[1]))
        else:
            os.system("cd ../dependency/platform-tools-macos && ./adb shell input tap " +
                      str(pos[0])+' '+str(pos[1]))

    if mType == '0'or mType == '3':
        # python
        print("python start")
        import jump_python.jumper as j
        dis = j.jumper()
        # print(dis)
        pass
    elif mType == '1' or mType == '4':
        # cpp
        if os.path.isfile("./jump_cpp/output.txt"):
            os.remove("./jump_cpp/output.txt")
        if mType == '1':
            os.system("cd jump_cpp && jumper.exe")
        else:
            os.system("cd jump_cpp && ./jumper")
        with open("./jump_cpp/output.txt") as f:
            dis = f.readlines(0)[0]
        pass
    elif mType == '2' or mType == '5':
        # matlab
        eng.addpath("./jump_matlab", nargout=0)
        dis = eng.jumper()
        pass

# dis 为学生返回的距离
    print(dis)
    dis = float(dis)
    time = int(dis * 1.392)
    if mType == '0' or mType == '1' or mType == '2':
        os.system(
            "cd ../dependency/platform-tools-windows && adb.exe shell input swipe 800 800 800 800 {0}".format(time))
    else:
        os.system(
            "cd ../dependency/platform-tools-macos && ./adb shell input swipe 800 800 800 800 {0}".format(time))
