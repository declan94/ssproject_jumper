# 跳不停

信号与系统课程大作业 “跳不停”

## 安装模拟器与配置环境

参考 👉[模拟器](./dependency/README.md)

## 开始开发

请使用 `src` 文件夹进行开发

### 试一试！

打开模拟器，并在 `cmd` 或 `terminal` 中使用 `adb` 模拟按压

```shell
# Windows
./dependency/platform-tools-windows/adb.exe shell input swipe 500 1600 500 1700 500

# macOS
./dependency/platform-tools-macos/adb shell input swipe 500 1600 500 1700 500
```

看到触控效果了吗？

### 正式开始

更多 `adb` 使用方法及调试用的程序示例请参考 👉[调试程序示例](./src/README.md)

开发过程请使用调试程序

## 准备提交

在完成代码后，请使用 `test` 文件夹完成最终提交代码的整合

`test` 文件夹下的程序即为作业批改时使用的程序，务必确保在提交前跑通测试程序

具体方法请参考 👉[测试程序示例](./test/README.md)

## 注意事项

- 调用 `adb` 时请确认当前路径，并使用相对路径进行调用，如在 `src` 文件夹下，应使用 `../dependency/` 的相对路径

- 若使用 `Visual Studio` 进行调试，也请复制 `dependency` 文件夹到你的当前项目目录下

- 请注意单次跳跃的程序运行时间不能过长，否则批改程序会主动终止你的进程

- 请注意代码风格, 必要模块可加简要注释

- 如有任何使用问题, 可在 `Issues` 提交问题, 我们会尽快解决

## 示例程序

该示例程序由 `周相鑫` 同学提供，仅供参考

请参考 👉[示例程序](./example/README.md)
