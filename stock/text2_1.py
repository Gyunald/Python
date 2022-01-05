naver_closing_price = [474500 , 461500 , 501000 , 500500 , 488500]
a = naver_closing_price
print(a)
b = max(naver_closing_price)
c = min(naver_closing_price)
print(b)
print(c)
print('가격차 =' , b - c)
d = list(naver_closing_price)
print('수요일 종가 =' , d[2])
naver_closing_price2 = {'9/7 월' : 474500 , '9/8 화' : 461500 , '9/9 수' : 501000 , '9/10 목' : 500500 , '9/11 금' : 488500}
e = naver_closing_price2
print(e)
f = naver_closing_price2['9/9 수']
print(f)