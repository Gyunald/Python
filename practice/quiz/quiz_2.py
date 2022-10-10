from random import *
import random

a = random.sample(range(1,21),4)
b = a[:1]
c = a[1:]
print(f"""
-- 당첨자 발표 --
치킨 당첨자 : {b}
커피 당첨자 : {c}
-- 축하합니다 --
""")

# a = list(range(1,21))
# shuffle(a)
# b = sample(a, 4)
# c = b[:1]
# d = b[1:]
# print(f"""
# -- 당첨자 발표 --
# 치킨 당첨자 : {c}
# 커피 당첨자 : {d}
# -- 축하합니다 --
# """)
