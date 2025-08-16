# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 23:18
@Desc     : 
"""
import redis

r = redis.Redis(
    host="159.75.144.33",
    port=6379,
    password="shaozi777",  # 如果无密码，删掉这一行
    decode_responses=True
)



# 测试写入和读取
r.set('test_key', 'hello redis')
value = r.get('test_key')
print('Redis取到的值:', value)
'153489461/*:.;；'