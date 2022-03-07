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

import datetime

a = datetime.datetime.now()
b = a.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(b)
