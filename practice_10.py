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

# a = ['a','b','c']
# b = [1,2,3]
# c = {}

# for i in range(len(a)) :
#     c[a[i]] = b[i]
# print(c)

# limit = 100
# i = 1
# sum_value = 0
# while limit >= sum_value :
#     sum_value += i
#     i += 1

# print(f"{i}를 더할 때 {limit}를 넘으며 그 때의 값은 {sum_value}입니다.")

max_value = 0
a = 0 
b = 0

for i in range(1,100) :
    j = 100 - i
    print(f"{i} * {j} = {i * j}")

    if max_value < i * j :
        max_value = i * j
        a = i
        b = j
print(f"{a} * {b} = {max_value}")

