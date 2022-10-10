# def run_timing():
#     num_cnt = 0
#     input_cnt = 0
    
#     # while a := input("Enter 10 km run time: "):
#     while True:
#         a = input("Enter 10 km run time: ")
#         if not a: 
#             break
#         input_cnt += 1
#         num_cnt += float(a)
        
#     b = num_cnt / input_cnt 
#     print(f"Average of {b}, over {input_cnt} runs")
# run_timing()

def 부동소수점(n1,n2,n3):
    a = str(n1).index(".") + 1
    b = str(n1)[a - (n2 + 1):a] + str(n1)[a:a + n3]
    
    return b

print(부동소수점(1234.5678, 2, 3))

