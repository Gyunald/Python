# 1

from random import *

t = []
while 1 :
    a = int(random() * 46) #  a = int((random() * 46) + 1)
    if len(t) == 5 :
        break
    if a == 0 :
        continue
    if a not in t:
        t.append(a)   
t.sort()
print(t)

# 2

from random import *

t = []
while 1 :
    a = int((random() * 45) + 1)
    if len(t) == 5 :
        break
    if a not in t:
        t.append(a)   
t.sort()
print(t)