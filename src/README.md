# 调试程序示例

同学自行调试时使用的 C++ Python MATLAB 的程序示例  
或参考`/src`目录下example code的中的函数  
获取安卓模拟器截图`read_image()`  
按照输入的press_time持续点击安卓模拟器屏幕`click_screen()`  

## 调用系统命令

### C++

```c++
system("YOUR_COMMAND");
```

### Python

```python
# win
import os
os.system('YOUR_COMMAND')
# linux / mac 
import subprocess
subprocess.call('YOUR_COMMAND')
```

### MATLAB

```matlab
system('YOUR_COMMAND');
```

## 调用 adb 命令

参见示例代码 👆
