# def mysum(*items):
#     if not items:
#         return items
#     output = items[0]
#     for i in items[1:]:
#         output += i
    
#     return output

# print(mysum(10,20,30,40))
# print(mysum('a','b','c','d'))
# print(mysum([10,20,30],[40,50,60],[70,80]))

# def mysum_bigger_than(*items):
#     output = 0
#     for i in items[1:] :
#         if items[0] < i :
#             output += i
#     return output

# print(mysum_bigger_than(10,5,20,30,6))

def sum_numeric(*items):
    try:
        output = 0
        for i in items :
            if type(i) == int:
                output += i
            elif type(i) == str:
                i = int(i)
                output += i
                continue
            else:
                continue
        return output
           
    except ValueError:
        
        print("값 오류")
        

print(sum_numeric(10,20,'a','30','bcd'))