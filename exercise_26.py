def add (a,b):
    return a+b

def calc(to_solve):
    a = {"+" : add}

    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return a[op](first, second)

print(calc("+ 6 3"))

import operator

def calc(to_solve):
    a = {"+" : operator.add,
         "-" : operator.sub,
         "*" : operator.mul,
         "/" : operator.truediv,
         "**" : operator.pow,
         "%" : operator.mod
         }

    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return a[op](first, second)

print(calc("* 4 3"))