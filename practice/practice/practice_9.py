# dict = [
#     {'name': '구름','age': 5},
#     {'name': '초코','age': 3},
#     {'name': '아지','age': 1},
#     {'name': '호랑이','age': 1},
# ]

# for i in dict:
#     print(i)
#     print(f"{i['name']} {i['age']}살")


# numbers = [1,2,1,7,2,5,3,7,1,4,6,9,5,1,5,6,1,7,4,2,0,9,7,9,0,8,6,4,7,2,1]
# counter = {}

# for number in numbers :
#     if number in counter :
#         counter[number] += 1
#     else :
#         counter[number] = 1
# print(counter)

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for i in character :
    if type(character[i]) is dict :
        for j in character[i] :
            print(f"{j} : {character[i][j]}")
    elif type(character[i]) is list :
        for k in character[i] :
            print(f"{i} : {k}")
    else :
        print(f"{i} : {character[i]}")