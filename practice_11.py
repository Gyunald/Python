# class Student:
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
#     def output(self):
#         print(self.name, self.age)
#     def __eq__(self, studendt_2):
#         print("hi")
#         return self.age == studendt_2.age

# student = Student("A", 1)
# student.output()
# print(student == student)

# class Student:
#     count = 0
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age

#         Student.count += 1
#         print(f"{Student.count}번째 학생이 생성되었습니다.")
    
# student = [
#     Student("A", 1),
#     Student("B", 2),
#     Student("C", 3)
# ]
# print(f"현재 생성된 총 학생 수는 {Student.count}명 입니다.")


# class Student:
#     count = 0
#     students = []

#     @classmethod
#     def output(cls):
#         print("학생목록")
#         for student in cls.students:
#             print(str(student))

#     def __init__(self, name, korean, math, english, science) :
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#         Student.count += 1
#         Student.students.append(self)
    
#     def get_sum(self):
#         return  self.korean + self.math + self.english + self.science 

#     def get_average(self):
#         return self.get_sum() / 4
    
#     def __str__(self):
#         return f"{self.name},{self.get_sum()},{self.get_average()}"

# Student("A", 30, 40, 50, 60),
# Student("B", 50, 60, 70, 80),
# Student("C", 60, 70, 80, 90)

# Student.output()

# import datetime

# a = datetime.datetime.now()
# b = a.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# print(b)

# import os

# output = os.listdir(".")
# print("os.listdir():", output)
# print()

# print("# 폴더와 파일 구분하기")

# for path in output:
#     if os.path.isdir(path):
#         print("폴더 :", path)
    
#     else:
#         print("파일 :", path)


# import os

# # 폴더라면 또 탐색하기 
# # 재귀함수
# def read_folder(path):
#     output = os.listdir(path)

#     for item in output:
#         if os.path.isdir(path + "/" + item):
#             read_folder(path + "/" + item)
        
#         else :
#             print("파일 :", item)
        
# read_folder(".")


# from urllib import request
# from bs4 import BeautifulSoup
# content = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
# soup = BeautifulSoup(content, "html.parser")

# for data in soup.select("data"):
#     print("시간 :", data.select_one("tmef").string)
#     print("날씨 :", data.select_one("wf").string)
#     print("-" * 20)


import text_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))