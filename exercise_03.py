def run_timing():
    num_cnt = 0
    input_cnt = 0
    
    # while a := input("Enter 10 km run time: "):
    while True:
        a = input("Enter 10 km run time: ")
        if not a: 
            break
        input_cnt += 1
        num_cnt += float(a)
        
    b = num_cnt / input_cnt 
    print(f"Average of {b}, over {input_cnt} runs")
run_timing()
