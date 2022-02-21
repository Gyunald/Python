# a = [1,2,3,4,5]
# c = 0
# for i in a :
#     c += 1
#     print(f"{c}번째 반복 : {i}")

# a = [1,2,3,4,5]

# for i in range(len(a)) :
#     print(f"{i}번째 반복 : {a[i]}")

# for i in range(4, 0-1, -1) :
#     print(i)

# for i in reversed(range(5)):
#     print(i)

a = ['a','b','c']
b = [1,2,3]
c = {}

for i in range(len(a)) :
    c[a[i]] = b[i]
print(c)