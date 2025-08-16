import re

import json

a= 'https://hz.lianjia.com/ershoufang'
b = 'https://hz.lianjia.com/ershoufang/pg100/'

c = '/'.join(a.split('/')[0:4])
d = '/'.join(b.split('/')[0:4])
print(c)
print(d)

e = b.split('/')[2]
print(e)
# num = int(re.search(r'pg(\d+)', a).group(1))+1# 匹配 pg 后面的数字

with open('', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k,v in data.items():
    if e in k:
        print(v)



# if num:
#     print(num)  # 输出: 100