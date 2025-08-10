# TOOL_ALL项目开源须知
## 一、你的权限

* 注意你的克隆和使用！！
* *  克隆后仅供个人学习使用， **禁止再分发！**
* * 注意本代码参照Apache License 2.0注意如下
* * 在分发IDEA Redis Client或其修改版本时，必须保留原作者的版权声明、许可声明以及许可证文本。
* * 不得以任何方式限制其他用户合法使用IDEA Redis Client，包括不得设置技术障碍、不得收取许可费用等。
* * 在分发IDEA Redis Client时，必须确保所有接收者都能获得Apache License 2.0的副本，并了解其在该许可证下的权利和义务。

2. 注意署名，如果要改进提交请提交合并！

## 二、代码
1. 注意！代码包含如下依赖库
   你可以使用如下代码安装这些库：
````cmd
pip install <库>
````
2023.8.4日志：**目前最新版本代码支持缺失库自动补全，如果依旧报缺库异常请手动下载**
代码如下：

需要的库（导入库部分代码）如下：

main.py
````python
from tqdm import *
````

cmd_args.py
````python
import argparse
import sys
import time
import os
from tqdm import *
````
ncmtomusic.py
```python
import binascii
import struct
import base64
import json
import os
from Crypto.Cipher import AES
```

## 三、版权声明
1. 声明
        **版权泠溪所有！**
2. 版权文件具体参考：**LICENSE文件！**

## 四、关于BUG
遇到bug请提交至项目反馈或者提交合并

## 五、关于
**copyright @Qin_Qiu_Fox at 2023 year**
**copyright @Qin_Qiu_Fox at 2024 year**
**copyright @Qin_Qiu_Fox at 2024.10**