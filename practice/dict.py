cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
 
# print(cabinet.get(3))
# # print(cabinet[5]) 에러
# print(cabinet.get(5)) # 키값이 없어도 none 표기
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"]) # str도 가능
print(cabinet["B-100"])

# 새손님
print(cabinet)
cabinet["C-20"] = "조세호" # 추가
cabinet["A-3"] = "김종국" # 덮어쓰기
print(cabinet)

# 간손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# valus 들만 출력
print(cabinet.values())

# 쌍으로 출력
print(cabinet.items())

# 지우기
cabinet.clear()
print(cabinet)