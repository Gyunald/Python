cur_price = {}
print(type(cur_price))
cur_price['apple'] = 10000 
cur_price['tesla'] = 20000
cur_price['naver'] = 50000
print('len =' , len(cur_price))
print("cur_price['apple'] =" , cur_price['apple'])
print(cur_price)
cur_price2 = {'samsung' : 100000 , 'lg' : 70000 , 'sk' : 50000 , 'posco' : 30000}
print(cur_price2)
del cur_price2['sk']
print(cur_price2)
print('(dic)' , cur_price2.keys())
stock_list = list(cur_price2.keys())
print('(list)' , stock_list)
print('(value)' , cur_price2.values())
price_list = list(cur_price2.values())
print('(list)' , price_list)
print("'sk' in cur_price2.keys()' =" , 'sk' in cur_price2.keys())
print("'posco' in cur_price2.keys() =" , 'posco' in cur_price2.keys())
