# 1,2,3,4,5 에 100씩 더하기
num = list(range(6))
num = [i + 100 for i in num]
print(num) 

name = ["1sbwq3s", "1shs3fjfj613", "1sjdj6h2sdfh45"]
name = [len(i) for i in name]
print(name)

name_2 = ["asada", "cbxbvvb", "qqrtwreyqry"]
name_2 = [i.upper() for i in name_2]
print(name_2)