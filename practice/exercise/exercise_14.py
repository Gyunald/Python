# menu = {"chicken" : 20, "sandwich" : 10 , "tea" : 7, "coke" : 5}

# def restaurant():
#     cost = 0
#     while order := input("Order: ") :
#         if order not in menu:
#             print("없는 메뉴입니다")
#         else:
#             cost += menu[order]
#             print(f"{order} costs {menu[order]}, total is {cost}")
#         print(f"Your total is {cost}")

# if __name__ == "__main__" :
#     restaurant()

user = {"kyu" : "ggg"}

def login():
    while name := input("아이디를 입력하세요."):
        
        if name in user :
            password = input("비밀번호를 입력하세요.")
            if password == user[name]:
                print("로그인 성공!")
                break
            else :
                print("로그인 실패!")

        else:
            print("아이디를 확인하세요.")
d= login()
d