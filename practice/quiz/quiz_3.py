from random import *
import random

# c = 1
# f = []

# # t = list(range(5,15+1))
# while c < 50 + 1 :
#     t = randrange(5,50+1)
#     if  5 <= t <= 15 :
#         print(f"[O] {c}번째 손님 (소요시간 : {t}분)")
#         f.append(c)
#         c += 1

#     elif t > 15 :
#         print(f"[X] {c}번째 손님 (소요시간 : {t}분)")
#         c += 1

# print(f"총 탑승 승객 {len(f)}분")


l = []
for i in range(1,51) :
    a = randrange(5,51)
    if 5 <= a <= 15 :
        print(f"[O] {i}번째 손님 (소요시간 : {a}분)")
        l.append(i)
    else :
        print(f"[X] {i}번째 손님 (소요시간 : {a}분)")
print(f"총 탑승 승객 : {len(l)}분")
