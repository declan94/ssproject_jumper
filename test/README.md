# 测试程序示例

test.py 为调用学生程序的主模块

## 使用

### Python

将你的 `Python` 程序入口所在文件命名为 `jumper.py` 且程序入口函数名应为 `jumper`，返回值为按压时间（以 ms 计，且为整数），在 `test` 目录下调用 `python test.py python` 开始测试

### MATLAB

将你的 `MATLAB` 程序入口所在文件命名为 `jumper.m` 且程序入口函数名应为 `jumper`，返回值为按压时间（以 ms 计，且为整数），在 `test` 目录下调用 `python test.py matlab` 开始测试

### C++

将你的 `C++` 程序源文件、头文件放置于 `jump_cpp` 文件夹中以便检查，再将以 `release` 方式编译的可执行文件重命名为 `jumper.exe`（Windows） 或 `jumper`（macOS）同样放置于该文件夹中，程序最后应输出按压时间（以 ms 计，且为整数），并且返回值为 `0`，在 `test` 目录下调用 `python test.py cpp` 开始测试

## 注意事项

- 你可以在 `jumper_cpp` 等这类文件夹中放置自己需要的其他文件，并以相对路径方式使用它们

- 注意程序的返回值或输出值应为 `int` 整数

## MATLAB 相关

如果你使用 `MATLAB` 编程，需要先安装用于 `Python` 的 `MATLAB 引擎 API`

MATLAB 提供了标准的 Python setup.py 文件，用于通过 distutils 模块编译和安装引擎。您可以使用相同的 setup.py 命令在 Windows®、Mac 或 Linux® 系统上编译和安装引擎

在安装之前，确认您的 Python 和 MATLAB 配置

- 您的系统具有受支持的 Python（建议使用较新版本） 和 MATLAB R2014b 或更新版本。要检查您的系统上是否已安装 Python，请在操作系统提示符下运行 Python
- 将包含 Python 解释器的文件夹添加到您的路径（如果尚未在该路径中）
- 找到 MATLAB 文件夹的路径。启动 MATLAB，并在命令行窗口中键入 matlabroot。复制 matlabroot 所返回的路径

要安装引擎 API，请在操作系统提示符下执行以下命令，其中 matlabroot 是 MATLAB 文件夹的路径。您可能需要管理员权限才能执行这些命令。或者，使用在非默认位置安装用于 Python 的 MATLAB 引擎 API 中所述的非默认选项之一

- Windows

```shell
cd "matlabroot\extern\engines\python"
python setup.py install
```

- macOS

```shell
cd "matlabroot/extern/engines/python"
python setup.py install
```

## 分数检测原理

参考 👉[check_result 模块](./check_result/README.md)
