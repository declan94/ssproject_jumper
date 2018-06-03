不同语言的客户端实现示例放在这里

jump.py为调用学生函数的主模块

* 如果使用python，则需要修改jump_python文件夹中的jumper.py，然后在命令行输入```python jump.py 0```运行
* 如果使用C++，则需要修改jump_cpp文件夹中的jump.cpp，然后编译链接生成一个名为**jump.exe**的可执行文件，在命令行输入```python jump.py 1```运行
* 如果使用matlab，则需要修改jump_matlab文件夹中的jumper.m，然后在命令行输入```python jump.py 2```运行

# 注意
如果您使用C++编程，程序需要将最后计算的结果（两方块之间的距离）**保存在jump_cpp文件夹下的output.txt中**

如果您使用matlab编程，需要先安装用于python的matlab引擎API

MATLAB 提供了标准的 Python setup.py 文件，用于通过 distutils 模块编译和安装引擎。您可以使用相同的 setup.py 命令在 Windows®、Mac 或 Linux® 系统上编译和安装引擎。

在安装之前，确认您的 Python 和 MATLAB 配置。

* 您的系统具有受支持的 Python（建议使用较新版本） 和 MATLAB R2014b 或更新版本。要检查您的系统上是否已安装 Python，请在操作系统提示符下运行 Python。
* 将包含 Python 解释器的文件夹添加到您的路径（如果尚未在该路径中）。**即可以通过命令行调用python脚本。**
* 找到 MATLAB 文件夹的路径。启动 MATLAB，并在命令行窗口中键入 matlabroot。复制 matlabroot 所返回的路径。

要安装引擎 API，请在操作系统提示符下执行以下命令，其中 matlabroot 是 MATLAB 文件夹的路径。您可能需要管理员权限才能执行这些命令。或者，使用在非默认位置安装用于 Python 的 MATLAB 引擎 API 中所述的非默认选项之一。

* windows
  ```
  cd "matlabroot\extern\engines\python"
  python setup.py install
  ```
* mac
  ```
  cd "matlabroot/extern/engines/python"
  python setup.py install
  ```
