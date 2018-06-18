# ssproject_jumper

Platform for the Project Homework of Signal and System Lesson -- Wechat Jumper Game Robot

## 模拟器安装与使用

参考 👉[模拟器](./dependency/README.md)

## 调试程序示例

参考 👉[调试程序示例](./src/README.md)  
开发过程请使用调试程序

## 测试程序示例

参考 👉[测试程序示例](./test/README.md)  
在提交前请跑通测试程序

## 提交方式

- 提交时请在 src 文件夹下仅保留需要提交的代码版本  
  例如:  
  需要提交 MATLAB 版本的代码,则在`src`文件夹下仅保留`jump_matlab`
- 注意,程序的入口文件命名方式请详见[调试程序示例](./src/README.md)
- 代码所调用的其他文件请全部置于`src`文件夹下,并使用 **相对路径**

## debug 方式

建议在获取图片之后, 将自己的检测的位置 Plot 在获取的图片上, 再将图片打印

## 注意事项

- 程序中 pause/sleep/press_time 的时间请不要设置的过小或过大, 在测试程序里面有针对此设计异常处理, 请合理设置 pause/sleep/press_time 时间,以免无法在测评获得游戏得分
- 在程序运行过程中,可以在`src`文件夹下读写文件, 请不要恶意写入过大/大量的文件
- baseline 仅为参考, 为大家提供 **获取模拟器截屏** 和 **点击模拟器** 的函数参考(请注意自己的操作系统 windows/macos,在示例代码里有相关说明), 思路不具备任何参考意义
- 请注意代码风格, 必要模块可加简要注释
- 如有任何使用问题, 可在 issue 提交问题, 我们会尽快解决
