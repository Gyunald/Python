def f(x):
    return (2 * x) + 1
print(f(10))

def f_2(x):
    return (x ** 2) + (x * 2) + 1
print(f_2(10))

def mul(*values):
    변수 = 1
    for i in values:
        변수 *= i
    return 변수        

print(mul(5,7,9,10))