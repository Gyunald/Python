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

# # 1~100을 2진수로 변환 후 0이 1개 포함된 수와 합.

# a = 0
# for i in range(1, 100 + 1):
#     if f"{i:b}".count("0") == 1 :
#         a += i
#         print(f"{i} : {i:b}")
# print(f"합계 : {a}")

# a = [ i for i in range(1, 100 + 1) if f"{i:b}".count("0") == 1 ]
# for i in a :
#     print(f"{i} : {i:b}")
# print(f"합계 : {sum(a)}")

# def a (*values, n=2) :
#     for i in range(n):
#         for value in values :
#             print(value)
#         print()
# a("a", "b", "c", n=3)


# # 리턴값을 가지고 리턴
# def return_test() :
#     return 100

# value = return_test()
# print(value)

# def f(x):
#     return (2 * x) + 1
# print(f(10))


# def f1(x1) :
#     return (x1 ** 2) + (2 * x1) + 1
# print(f1(10))
# # 5,7,9,10 을 가변 매개변수로 모두 곱한 값을 리턴하는 함수

# def mul(*values) :
#     i = 1
#     for j in values :
#         i *= j
#     return i
# print(mul(5, 7, 9, 10))

# def factorial(n):
#     output = 1
#     for i in range(1, n + 1):
#         output *= i
#     return output

# print(factorial(6))

# def factorial(n):
#     if n == 0 :
#        return 1

#     else :
#         return n * factorial(n - 1)

# print(factorial(5))


# def fibonacci(n) :
# #피보나치 수를 구합니다.
#     if n == 1 :
#         return 1
#     if n == 2 :
#         return 1
#     else :
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(5))

# a = {
#     1 : 1,
#     2 : 1,
# }

# def fibonacci(n):
#     if n in a :
#         # 메모가 되어 있으면 메모된 값을 리턴
#         return a[n]
    
#     # 메모가 되어 있지 않으면 값을 구함 (메모를 함)
#     a[n] = fibonacci(n - 1) + fibonacci(n - 2)
#     return a[n]
# print(fibonacci(10))


# def number_input():
#     output = float(input("숫자를 입력하세요 > "))
#     return output
# def get_circumference(radius):
#     return 2 * 3.14 * radius
# def get_circumarea(radius):
#     return 3.14 * radius * radius

# radius = number_input()
# print(round(get_circumference(radius),2))
# print(round(get_circumarea(radius),2))

# # 코드 유지보수를 위해 변수를 활용
# def p(content):
#     return f"<p class ='content-line'>{content}</p>"
# # 아래 한 줄씩 다 바꿔줄 필요없이 위 함수에 변수만 바꿔주면 모두 적용
# print(p("안녕하세요"))
# print(p("간단한 HTML 태그를 만드는 중입니다."))

# def flatten(data):
#     output = []
#     for i in data:
#         if type(i) == list:
#             output += flatten(i)
#         else:
#             output += [i]
#     return output

# example = [[1, 2, 3], [4, [5, 6]], [7, [8, 9]]]
# print(example)
# print(flatten(example))

min_to_seat = 2
max_to_seat = 10
all_people = 100
memo = {}

def do(rest_people, seated_people):
    key = rest_people,seated_people
    if key in memo :
        return memo[key]
    if rest_people < 0 :
        return 0
    if rest_people == 0 :
        return 1
    
    count = 0
    for i in range(seated_people, max_to_seat + 1) :
        count += do(rest_people - i, i)

    memo[key] = count
    return count
print(do(100,2))
    