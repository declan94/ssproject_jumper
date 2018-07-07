# 测试程序示例

test.py 为调用学生程序的主模块

## test 目录说明

### ground_truth

此文件夹下放置距离给出的示例，参考 [距离示例](./ground_truth/README.md)

### upload_example

此文件夹下放置提交的压缩包示例

### upload_template

此文件夹下放置提交的源代码模板和报告模板

## 提交

- 你的作业应以 `zip 压缩文件` 的形式提交并以学号命名，如 `2016010000.zip`，不允许使用 `rar 压缩文件`，提交示例参考 [upload_example](./upload_example)

- 该压缩文件打开后，应为单个文件夹且以学号命名，如 `2016010000`

- 在该文件夹下，应包含 `两个文件夹` 和 `一个报告`

  - 报告以 `班级_学号_姓名` 形式命名，如 `无61_2016010000_张三.pdf`，报告示例参考 [report.pdf](./upload_template/report.pdf)

  - 一个文件夹为 `pictures`，其中存放你的标注图片，标注图片均以 `学号_图片序号_四舍五入整数距离真值_目标块半径.png` 命名，如 `2016010000_1_234_50.png`，只允许提交 `png 图片`，并且保证图片 `边缘完整`，参考 [upload_example](./upload_example)

  - 另一个文件夹为 `python` （或 `matlab`、`cpp`），取决于你使用的语言，不允许提交多个此类文件夹（如同时提交了 `python` 和 `cpp` 文件夹），参考 [upload_example](./upload_example) 和 [upload_template](./upload_template)

### Python

将你的 `Python` 程序入口所在文件命名为 `jumper.py` 且程序入口函数名应为 `jumper`，返回值为距离（以像素点计，且为整数）

模板程序已在 `test/src/python` 目录下给出，可参考

你的提交文件结构大致如下

```
- 2016010000.zip
  - 2016010000
    - 无61_2016010000_张三.pdf
    - picture
      - 2016010000_1_234_50.png
      - 2016010000_2_234_50.png
      - 2016010000_3_234_50.png
      ...
    - python
      - jumper.py
      - __init__.py
      ... 其他需要用到的文件
```

注意务必不要删除 `__init__.py`

### MATLAB

将你的 `MATLAB` 程序入口所在文件命名为 `jumper.m` 且程序入口函数名应为 `jumper`，返回值为距离（以像素点计，且为整数）

模板程序已在 `test/src/matlab` 目录下给出，可参考

你的提交文件结构大致如下

```
- 2016010000.zip
  - 2016010000
    - 无61_2016010000_张三.pdf
    - picture
      - 2016010000_1_234_50.png
      - 2016010000_2_234_50.png
      - 2016010000_3_234_50.png
      ...
    - matlab
      - jumper.m
      ... 其他需要用到的文件
```

### C++

将你的 `C++` 程序源文件、头文件放置于 `jump_cpp` 文件夹中以便检查，再将以 `release` 方式编译的可执行文件重命名为 `jumper.exe`（Windows） 或 `jumper`（macOS）同样放置于该文件夹中，程序最后应输出距离（以像素点计，且为整数）并且返回值为 `0`

模板程序已在 `test/src/cpp` 目录下给出，可参考

你的提交文件结构大致如下

```
- 2016010000.zip
  - 2016010000
    - 无61_2016010000_张三.pdf
    - picture
      - 2016010000_1_234_50.png
      - 2016010000_2_234_50.png
      - 2016010000_3_234_50.png
      ...
    - cpp
      - jumper.cpp
      - jumper.h（非必需，取决于你的代码结构）
      - jumper.exe (jumper) （Release 模式编译）
      ... 其他需要用到的文件
```

## 自行检查

1.  将标注好的图片放置在 `test/pictures` 文件夹（请自行新建）中，将压缩包放置在 `test/uploads` 文件夹（请自行新建）中

2.  在 `test` 目录下，调用 `python test.py` 开始测试

## 注意事项

- 你可以在 `python` 等这类文件夹中放置自己需要的其他文件，并以相对路径方式使用它们

- 注意程序的返回值或输出值应为四舍五入的 `int` 整数

### MATLAB 相关

需要使用 `test.py` 对 `MATLAB` 程序进行验证的同学请参考 👇

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
