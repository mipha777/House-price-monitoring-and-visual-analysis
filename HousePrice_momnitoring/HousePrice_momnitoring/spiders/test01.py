# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/16 05:11
@Desc     : 
"""
import re

import json

a= 'https://hz.lianjia.com/ershoufang'
b = 'https://hangzhou.anjuke.com/sale/?from=HomePage_TopBar'

c = '/'.join(a.split('/')[0:4])
d = '/'.join(b.split('/')[0:4])
print(c)
print(d)

e = b.split('/')[2]
print(e)
# num = int(re.search(r'pg(\d+)', a).group(1))+1# 匹配 pg 后面的数字



# if num:
#     print(num)  # 输出: 100