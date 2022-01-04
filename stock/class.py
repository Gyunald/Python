class stock :
    market = "kospi"
print(dir())
print(stock)
print(stock.__dict__)
print(stock.market)
s1 = stock()
s2 = stock()
print(id(s1))
print(id(s2))
print(dir())
print(s1.__dict__)
print(s2.__dict__)
s1.market = "kosdaq"
print(s1.__dict__)
print(s1.market)
print(s2.market)