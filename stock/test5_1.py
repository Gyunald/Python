def myaverage(a,b) : 
    return (a + b) / 2
print(myaverage(5,3))

def get_max_min(num) :
    max1 = max(num)
    min1 = min(num)
    return (max1 , min1)
max1 , min1 = get_max_min([1,2,3,4,5,6,7])    
print(max1)
print(min1)

import os
def get_test_list(path) :
    list_a = os.listdir(path)
    word = []
    for i in list_a :
        if i.endswith("html") :
            word.append(i)
    return word
print(get_test_list("/Users/kyu-deokkim/Documents/HTML/web"))

def cal_bmi(weight, height):
    height = height * 0.01
    bmi = weight / (height * height)
    if bmi < 18.5:
            print("마른체형")
    elif 18.5 <= bmi < 25.0:
            print("표준")
    elif 25.0 <= bmi < 30.0:
            print("비만")
    else:
            print("고도비만")
print(cal_bmi(80 , 180))
print(cal_bmi(66 , 174))

def cal_bmi2(height, weight):
    height = height * 0.01
    bmi = weight / (height * height)
    print("BMI: ", bmi)
    if bmi < 18.5:
            print("마른체형")
    elif 18.5 <= bmi < 25.0:
            print("표준")
    elif 25.0 <= bmi < 30.0:
            print("비만")
    else:
            print("고도비만")
while 1:
    height = input("Height (cm): ")
    weight = input("Weight (kg): ")
    cal_bmi2(float(height), float(weight))