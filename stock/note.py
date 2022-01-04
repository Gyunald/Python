cur_price = 9980
if cur_price >= 5000 and cur_price > 10000:
    print("Buy 100")
else:
    print("Sell 100")
for i in range(0, 11, 3):
    print(i)
interest_stocks = ["naver" , "samsung" , "sk" , "hanhwa" , "kakao"]
del interest_stocks [3]
for company in interest_stocks:
    print(f"{company} : buy 10")
