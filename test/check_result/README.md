# check_result 模块

## check_result 模块的使用方法

- 1 在需要检测游戏是否结束并且在游戏结束的时候得到成绩的模块中 import check_reuslt 模块
- 2 调用函数 check_result(img)，参数是用 opencv 读取的一在模拟器中用 adb 截取的当前状态的图片，返回值是 n,position,其中 n≥-1 并且 n 为整数。当 n=-1 时，代表游戏没有结束，继续进行,并且，此时的 position 一定是[None,None]。当 n≥=0 时，代表游戏结束，并且 n 的值就是本局游戏的成绩,并且 position 的值就是去点击的重新开始的位置。

## check_result 模块的测试

- 1 当打出了新的记录的时候，分数的显示位置和显示方式都和一般情况下不同。本模块处理了这种情况，但由于相关数据较少，测试次数暂时不够。
