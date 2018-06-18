import sys
import os
import matlab.engine
import check_result
import cv2

# print(sys.argv)
mType = sys.argv[1]
dis = 0.0  # 学生返回的距离


while True:
    os.system(
        "cd ../dependency/platform-tools-windows && ./adb.exe shell screencap -p /sdcard/autojump.png")
    os.system(
        "cd ../dependency/platform-tools-windows && ./adb.exe pull /sdcard/autojump.png .")
    img = cv2.imread("./autojump.png")
    score, pos = check_result.check_result(img)
    if score >= 0:
        with open("./result.txt", a) as f:
            f.write("score:", score)
            f.write("\n")
        os.system(
            "cd ../dependency/platform-tools-windows && ./adb.exe shell input tap "+str(pos[0])+' '+str(pos[1]))
        pass

    if mType is '0':
        # python
        print("python start")
        import jump_python.jumper as j
        dis = j.jumper()
        # print(dis)
        pass
    elif mType is '1':
        # cpp
        if os.path.isfile("./jump_cpp/output.txt"):
            os.remove("./jump_cpp/output.txt")
        os.system("cd jump_cpp && jumper.exe")
        with open("./jump_cpp/output.txt") as f:
            dis = f.readlines(0)[0]
        pass
    elif mType is '2':
        # matlab
        eng = matlab.engine.start_matlab()
        eng.addpath("./jump_matlab", nargout=0)
        dis = eng.jumper()
        pass

# dis 为学生返回的距离
    print(dis)
    dis = float(dis)
    time = int(dis * 1000)
    os.system(
        "cd ../dependency/platform-tools-windows && ./adb.exe shell input swipe 800 800 800 800 {0}".format(time))
