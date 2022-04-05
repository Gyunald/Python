# def first_last(word):
#     first = word[:1]
#     last = word[-1:]
#     return first + last

# t1 = ("a","b","c")
# t2 = (1,2,3,4)
# print(first_last(t1))
# print(first_last(t2))

# def even_odd_sums(num):
#     a = sum(num[0:-1:2])
#     b = sum(num[1::2])
#     return [a,b]
# print(even_odd_sums([10,20,30,40,50,60]))

def myzip(num,word):
    return list(zip(num,word))
print(myzip([10,20,30],'abc'))