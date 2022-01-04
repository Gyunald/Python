# 표준 체중

def std_weight(height, gender) :
    if gender == "남자" :
        return (height / 100) * (height / 100) * 22
    elif gender == "여자" :
        return (height / 100) * (height / 100) * 21
    
    
height = 185
gender = "남자"
weight = round(std_weight(height,gender),2)
print(f"키 {height}cm 남자의 표준 체중은 {weight} 입니다")

# # 표준 체중

# def std_weight(height, gender) :
#     if gender == "남자" :
#         return (height / 100) * (height / 100) * 22
#     elif gender == "여자" :
#         return (height / 100) * (height / 100) * 21

# weight = round(std_weight(175,"남자"),2)
# height = ?
# print(f"키 {height}cm 남자의 표준 체중은 {weight} 입니다")