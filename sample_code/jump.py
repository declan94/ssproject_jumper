import sys
import os
import matlab.engine

# print(sys.argv)
mType = sys.argv[1]
dis = 0.0 # 学生返回的距离

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
    eng.addpath("./jump_matlab",nargout=0)
    dis = eng.jumper()
    pass

# dis 为学生返回的距离
print(dis)