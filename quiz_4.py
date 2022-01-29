def std_weight(height, gender):

    if gender == "남자" :
        return height * height * 22
      
    elif gender == "여자" :
        return  height * height * 21
        

height = 153
gender = "여자"
weight = std_weight(height*0.01, gender)
print(f"키 {height}cm {gender}의 표준 체중은 {round(weight,2)}kg 입니다")