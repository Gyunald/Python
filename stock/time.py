import time
a = time.time()
print(int(a))
b = time.ctime()
print(b)
print(type(b))
print(b.split(' ')[-1])

for i in range(3) :
    print(i)
    time.sleep(.3)

import random
print(random)
import time
print(dir(time))