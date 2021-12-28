import random

# list = []

# list.append(random.sample(range(5),5))
# print(list)
# random.sample은 list로 반환 리스트 내 리스트

list = random.sample(range(5),5)
print(list)

list_2 = []
for i in range(5):
    list_2.append(random.randrange(5))
    
print(list_2)
list_3 = [100,101,102,103,104]
list_2.pop() # 마지막 요소 삭제
list_2.extend(list_3)
list_2.sort() # 오름차순 정렬
print(list_2)