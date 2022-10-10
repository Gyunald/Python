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
#     a = []
#     for i in data:
#         if type(i) == list:
#             a += flatten(i)
#         else:
#             a += [i]
#     return a

# example = [[1,2,3],[4,[5,6]],7,[8,9]]
# print(example)
# print(flatten(example))

# 앉힐수있는최소사람수 = 2
# 앉힐수있는최대사람수 = 10
# 전체사람의수 = 100

# memo = {}

# def 문제(남은사람수, 앉힌사람수):
#     key = str([남은사람수, 앉힌사람수])

#     if key in memo:
#         return memo[key]
#     if 남은사람수 < 0:
#         return 0
#     if 남은사람수 == 0:
#         return 1

#     count = 0
#     for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
#         count += 문제(남은사람수 - i, i)
#     memo[key] = count
#     return count

# print(문제(100,2))

# a, b, c = 10 , 20 , 30
# a, b, c = c, b, a
# print(a,b,c)

# a, b = 333 , 55
# print(divmod(a,b)) # 몫, 나머지
# x,y = divmod(a,b) 
# print(x)
# print(y)

# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("hello")

# call_10_times(print_hello) # 매개변수로 함수를 전달

# def power(item):
#     return item * item

# def under_3(item):
#     return item < 3

# list_input_a = [1,2,3,4,5]
# # map = 결과값으로 새로운 리스트로 생성
# # filter = 결과값이 True인것만으로 새로운 리스트 생성
# list_output_a = map(lambda x : x * x, list_input_a) # 매개변수 : 리턴값
# print(list_output_a)
# print(list(list_output_a))

# list_output_b = filter(lambda x: x < 3, list_input_a)
# print(list_output_b)
# print(list(list_output_b))

# import random

# a = list("가나다라마바사아자차카타파하")
# with open("a.txt","w") as file:
#     for i in range(100):
#         name = random.choice(a) + random.choice(a)
#         weight = random.randrange(40, 100)
#         height = random.randrange(150, 200)
#         file.write(f"{name}, {weight}, {height}\n")

# with open("a.txt","r") as file:
#     for line in file:
#         (name, weight, height) = line.strip().split(", ") #
        
#         if not name or not weight or not height :
#             continue

#         bmi = int(weight) / ((int(height) / 100 ) ** 2)
        
#         result = ""

#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi: 
#             result = "정상체중"
#         else :
#             result = "저체중"
            
#         print(f"\n".join
#         ([f"""
#         이름 : {name}
#         몸무게 : {weight}
#         키 : {height}
#         BMI : {round(bmi,2)}
#         결과 : {result}"""]))

# def test():
#     print("A")
#     yield 1
#     print("B")
#     yield 2
#     print("C")

# output = test()
# print("D")
# a = next(output)
# print(a)
# print("E")
# b = next(output)
# print(b)
# print("F")
# c = next(output) # next()호출 이후 yield 키워드를 만나지 못하고 끝나면 예외
# print(c)
# next(output)

# numbers = [1,2,3,4,5,6]
# print("::".join(
#     map(str, numbers)
#     ))

# numbers = list(range(1, 10 + 1))
# print("홀수만 추출하기")
# print(list(filter(lambda x : x % 2 == 1, numbers)))
# print()
# print("3 이상, 7 미만 추출하기")
# print(list(filter(lambda x : 3 <= x < 7, numbers)))
# print()
# print("제곱해서 50 미만 추출하기")
# print(list(filter(lambda x : (x ** 2) < 50, numbers)))

# list_input_a = "1","2","3","A", 4

# list_numbers = []

# for item in list_input_a :
#     try :
#         float(item)
#         list_numbers.append(item)
#     except :
#         pass
# print(list_input_a)
# print(list_numbers)

# def test():
#     print("start")
#     try:
#         print("try")
#         return
#         print("try_2")
#     except:
#         print("except")
#     else:
#         print("else")
#     finally:
#         print("finally")
#     print("test")
# test()

# # 조건문을 사용
# import random

# numbers = [52, 273, 32, 103, 90, 10, 275]
# a = random.choice(numbers)

# print("(1) 요소 내부에 있는 값 찾기")
# print(f"{a}는 {numbers.index(a)} 위치에 있습니다.")
# print()

# print("(2) 요소 내부에 없는 값 찾기")
# number = 10000
# if number in numbers :
#     print(f"{number}는 {numbers.index(number)} 위치에 있습니다.")

# else:
#     print("리스트 내부에 없는 값입니다.")
#     print()
# print("정삭적으로 종료되었습니다.")

# try except 사용

# import random

# numbers = [52, 273, 32, 103, 90, 10, 275]
# a = random.choice(numbers)
# print("(1) 요소 내부에 있는 값 찾기")
# print(f"{a}는 {numbers.index(a)} 위치에 있습니다.")
# print()

# print("(2) 요소 내부에 없는 값 찾기")
# number = 10000
# try :
#     print(f"{number}는 {numbers.index(number)} 위치에 있습니다.")
# except:
#     print("리스트 내부에 없는 값입니다.")
#     print()
# finally:
#     print("정삭적으로 종료되었습니다.")

