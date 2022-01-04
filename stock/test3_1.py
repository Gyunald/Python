apart = [[101,102,103],[201,202,203],[301,302,303,],[401,402,403]]
arrears = [101,203,301,403]
for floor in apart :
    for room in floor :
        if room in arrears :
            continue
        else :
            print("delivery:", room)
for j in range(6) :
    print("*", end="")
print()
for j in range(4) :
    for i in range(5) :
        print("*", end="")
    print()
for j in range(5) :
    for i in range(j+1) :
        print("*", end="")
    print()
for j in range(5) :
    for i in range(5-j) :
        print("*" , end="")
    print()
for j in range(5) :
    for i in range(4-j) :
        print(" ", end='')
    for k in range(j+1) :
        print("*", end='')
    print()
for j in range(5) :
    for i in range(j) :
        print(" ", end="")
    for i in range(5-j) :
        print("*" , end="")
    print() 
for j in range(5) :
    for i in range(4-j) :
        print(" ", end="")
    for i in range(j) :
        print("*", end="")
    for i in range(j+1) :
        print("*", end="")
    print()
for j in range(5) :
    for i in range(j) :
        print(" ", end="")    
    for i in range(4-j) :
        print("*", end="")
    for i in range(5-j) :
        print("*", end="")
    print()
print("----------------")
print("----------------")
print("----------------")
for j in range(5):
        for i in range(4-j):
                print(' ', end='')
        for i in range(2*(j+1)-1):
                print('*', end='')
        print()
for j in range(5):
        for i in range(j):
                print(' ', end='')
        for i in range(2*(5-j)-1):
                print('*', end='')
        print()