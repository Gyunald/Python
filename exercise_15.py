from collections import Counter

def get_rainfall():
    city_list = {}
    li = []
   
    while city := input("도시를 입력하세요."):
        if city :
            li.append(city)
            a = Counter(li)
        precipitation = int(input("강수량을 입력하세요."))
        city_list[city] = city_list.get(city, 0) + int(precipitation)

    print(a)
    b = list(a.values())
    c = 0
    for i,j in city_list.items():
        print(f"{i} : {j} , ave : {j/b[c]}")
        c += 1 

if __name__ == "__main__" :
    get_rainfall()