from random import *

# a = random.sample(range(21),3)
# print(a)

a = list(range(1,20+1))
print(a)
shuffle(a)

winner = sample(a,4)


print(f"치킨 당첨자{winner[:1]}")
print(f"커피 당첨자{winner[1:]}")
