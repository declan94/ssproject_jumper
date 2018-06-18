# 模拟器

- [安装](#安装)
  - [Windows](#windows)
  - [Mac](#mac)
- [使用](#使用)
  - [打开小程序](#打开小程序)
  - [使用 adb](#使用-adb)

## 安装

### Windows

#### 系统要求

- Microsoft Windows 7, 8/8.1, 10 (32/64 位)

- 64 位 CPU, 支持硬件虚拟化技术（且已在 BIOS 中开启此功能）`原则上第四代酷睿及以上的 Intel CPU 均支持此技术`

- 至少 2GB 内存

#### 准备工作

- 下载 [Android Emulator](https://cloud.tsinghua.edu.cn/f/e1548fc6fdec474091bb/) 并 `解压`

#### 开始安装

- 安装 `Android Emulator` 文件夹下的 `VirtualBox-5.2.12-122591-Win.exe`，在弹出的 `安装设备` 窗口均选择 `是`，完成安装后关闭 `VirtualBox`

- 继续安装 `genymotion-2.12.1.exe`，安装结束后打开程序，在弹出的窗口中点击最下方的 `Personal Use`，不需要输入账户密码，进入主界面后关闭 `Genymotion`

#### 导入模拟器

- 进入 `开始菜单` 或者 `桌面`，打开 `Oracle VM VirtualBox`，点击左上角的 `管理`，再选择 `导入虚拟电脑`，文件选择 `Android Emulator` 文件夹下的 `Google Nexus 5X - 6.0.0 - API 23 - 1080x1920.ova`，按默认设置导入即可

#### 设置模拟器并启动

- 打开 `Genymotion`，选择 `Google Nexus 5X - 6.0.0 - API 23 - 1080x1920` 右侧的 🔧 图标，根据自己系统配置调整 `Processor`（CPU 核心数） 与 `Base Memory`（分配给模拟器的内存） 的设置，两项设置均不能超过当前硬件水平，请勿更改其他设置，完成后注意确定保存

- 选中当前模拟器，并点击 `Start`，等待模拟器启动

- 微信就在主屏幕正中间，Congrats!

### Mac

#### 系统要求

- MacOSX

- 至少 2GB 内存, 剩余磁盘空间 400MB 以上

#### 准备工作

- 下载 [Android Emulator](https://cloud.tsinghua.edu.cn/f/ab7a837b0e294e4e9c2f/) 并 `解压`

#### 开始安装

- 打开 `Android Emulator` 文件夹下的 `VirtualBox-5.2.12-122591-OSX.dmg`，在弹出的窗口中，打开`VirtualBox.pkg`，按照指示安装，安装过程中可能需要输入密码；另外，可能会遇到涉及 Security 的问题导致安装失败，这时打开`System Preferences/系统偏好设置`中`Security & Privacy/安全性与隐私`，点击右下角的`Allow/允许`，然后重新安装即可

- 打开 `genymotion-2.12.1.dmg`，将弹出窗口中的`Genymotion.app`和`Genymotion Shell.app`拖入`Applications`文件夹中即可，复制完成后打开程序，在弹出的窗口中点击最下方的 `Personal Use`，之后不需要输入账户密码，直接进入主界面后关闭 `Genymotion`

#### 导入模拟器

- 进入 `launchpad/启动台`，打开 `VirtualBox`，点击屏幕顶端菜单栏的 `File/管理`，再选择 `Import Appliance/导入虚拟电脑`，文件选择 `Android Emulator` 文件夹下的 `Google Nexus 5X - 6.0.0 - API 23 - 1080x1920.ova`，按默认设置导入即可

#### 设置模拟器并启动

- 打开 `Genymotion`，选择 `Google Nexus 5X - 6.0.0 - API 23 - 1080x1920` 右侧的 🔧 图标，根据自己系统配置调整 `Processor`（CPU 核心数） 与 `Base Memory`（分配给模拟器的内存） 的设置，两项设置均不能超过当前硬件水平，请勿更改其他设置，完成后注意确定保存

- 选中当前模拟器，并点击 `Start`，等待模拟器启动

- 微信就在主屏幕正中间，Congrats!

## 使用

### 打开小程序

- 进入微信，此时微信申请权限，请均同意

- 登录微信后，点击右上角的 🔍 图标，在搜索栏输入 `tiaoyitiao`，点击 `跳一跳` 小程序即可打开

### 使用 adb

使用 `adb` 命令实现截图获取和保存以及模拟按压功能

`adb` 的可执行文件位于 [platform-tools-windows](./platform-tools-windows) (Windows) 和 [platform-tools-macos](./platform-tools-macos) (mac OS)

`macOS` 在执行 `adb` 前可能需要设置可执行权限 `chmod +X /dependency/platform-tools-macos/adb`

#### 检验`adb`是否连接

如果已经连接，则会在`List of devices attached`下面显示已连接的设备信息

```shell
# Windows
./adb.exe devices

# macOS
./adb devices
```

#### `adb`连接到模拟器

如果`adb`未连接到设备，则需要执行以下命令

IP 在模拟器的标题栏中，如果看不到可以拉伸模拟器窗口，以显示出完整标题

```shell
# Windows
./adb.exe connect IP
#macOS
./adb connect IP
```

#### 执行截图

```shell
# Windows
./adb.exe shell screencap -p /sdcard/autojump.png

# macOS
./adb shell screencap -p /sdcard/autojump.png
```

#### 保存截图到本地

```shell
# Windows
./adb.exe pull /sdcard/autojump.png .

# macOS
./adb pull /sdcard/autojump.png .
```

#### 模拟触控位置与时间

```shell
# Windows
./adb.exe shell input swipe x y x y time(ms)

# macOS
./adb shell input swipe x y x y time(ms)
```
