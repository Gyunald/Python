import random

def get_n():
    num = random.randint(1,45)
    return num

lotto_num = []
count = 0

while True :
    if count > 5  :
        break
    n = get_n()
    if get_n not in lotto_num :
        lotto_num.append(n)    
        lotto_num.sort()
        count += 1
print(lotto_num)