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

# max_value = 0
# a = 0 
# b = 0

# for i in range(1,100) :
#     j = 100 - i
#     print(f"{i} * {j} = {i * j}")

#     if max_value < i * j :
#         max_value = i * j
#         a = i
#         b = j
# print(f"{a} * {b} = {max_value}")

# a = ["a", "b", "c"]

# for i, b in enumerate(a) :
#     print(i,b)

# a = {"a" : 1, "b" : 2, "c" : 3 }

# for i, j in a.items() :
#     print(i, j)

# # 리스트 내포 (list comprehensions)
# a = []
# b = range(0, 20 +1, 2)
# for i in b :
#     a.append(i * i)
# print(a)

# a = [i * i for i in b ]
# print(a)

# a = [ i * i for i in b if (i * i) % 2 == 0 ]
# print(a)

# # 괄호로 문자열 열결하기

# a = (
#     "이렇게 입력해도 "
#     "하나의 문자열로 연결되어"
#     "생성됩니다."
# )
# print(a)
# print(type(a))

# print((
#     "이렇게 입력해도 "
#     "하나의 문자열로 연결되어 "
#     "생성됩니다."
# ))

# print(" ".join([ # " " , "\n"
#     "이렇게 입력해도",
#     "하나의 문자열로 연결되어",
#     "생성됩니다."
#     ])
# )

# 2진수:b 8진수:o 16진수:x
# print("{:b}".format(10))
# print(f"{10:b}")

# # 1~100 사이 2진수러 변환 후 2진수에 0이 1개 포함된 수와 합.
# a = 0
# b = range(1, 100 + 1)
# for i in b :
#     if bin(i).count("0") == 2 :
#         a += i
#         print(f"{i} : {i:b}")

# print(f"합계 : {a}")

# a = [ i for i in range(1, 100 + 1) if bin(i).count("0") == 2 ]
# print(a)
# print(sum(a))

# a = 0
# for i in range(1, 100 + 1) :
#     if f"{i:b}".count("0") == 1 :
#         print(f"{i} : {i:b}")
#         a += i
# print(f"합계 : {a}")

a = [i for i in range(1, 100 + 1) if f"{i:b}".count("0") == 1 ]
for i in a :
    print(f"{i} : {i:b}")
print(f"합계 : {sum(a)}")