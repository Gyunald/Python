import os
a = os.getcwd()
print(a)

b = os.listdir()
print(b)

print(os.listdir("/Users/kyu-deokkim/Documents/2021/p"))
a = os.listdir("/Users/kyu-deokkim/Documents/2021/p")
b = []
print("사진 수 =", len(a))
print("타입 =", type(a))
for x in os.listdir("/Users/kyu-deokkim/Documents/2021/p") : 
    if x.endswith("jpeg") :
        b.append(x)
print("jpeg 파일 리스트 =" , b)
print("jpeg 파일 수 =" , len(b))