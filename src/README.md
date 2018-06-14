# 运行方式
请详见../test/文件夹下的文档

# debug模式(自定义程度较高, 不推荐使用, 较为繁琐)
可直接在本地机通过命令行调用adb命令,详细操作如下

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
