# def create_students(name, korean, math, english, science):
#     return {
#         "name" : name,
#         "korean" : korean,
#         "math" : math,
#         "english" : english,
#         "science" : science
#     }

# def student_get_sum(student):
#     return student["korean"] + student["math"] + student["english"] + student["science"]

# students = [
#     create_students("김규덕", 87, 98, 88, 95),
#     create_students("이진주", 92, 98, 96, 98)
# ]

# for student in students:
#     print(student_get_sum(student))


# class Student:
#     count = 0
#     def __init__(self,name,korean,math,english,science) -> None:
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science

#         Student.count += 1
#         print(f"{Student.count}번째 학생이 생성되었습니다.")

#     def get_sum(self):
#         return self.korean + self. math + self.english + self.science

#     def __str__(self):
#         return f"{self.name} {self.get_sum()}"

# students = [
#     Student("김규덕", 87, 98, 88, 95),
#     Student("이진주", 92, 98, 96, 98),
# ]

# for student in students:
#     # print(student.__str__())
#     print(str(student))
# print(f"현재 생성된 총 학생 수는 {Student.count}명 입니다. ")

# a = lambda x,y: x + y
# print((lambda x,y: x + y)(1,2))
# print(a(1,2))


class Car:#   <- Car라는 class를 만든것
    color = 'white'#    <- 변수
    def __init__(self):#  <- 생성자 : 주로 클래스의 객체가 생성될 때 
        self.displacement = 0#         인스턴트 멤버변수를 초기화하는 역할을 함
        self.door = 0#        생성자 안에서 인스턴스 멤버변수를 작성함
        self.gear_type = ''
        self.fuel = '가솔린'
        self.auto_navi = False

    def __str__(self) :#    <- __str__(self) : str메소드
        return f'{self.displacement}-{self.door}-{self.gear_type}-{self.fuel}'#주로 멤버변수들의 값을 문자열로 반환
#객체를 프린트하면 이 문자열이 출력됨

    @classmethod    
    def describe(cls):#  <- 클래스메소드 : @classmethod 데코레이터를 사용하고
        cls.auto_navi = True#parameter 에 (self)가 아닌 (cls)를 지정함
        print('describe(cls) 메소드는 Car 클래스의 클래스메소드입니다')    #    ㄴ인스턴스 멤버변수(self)는 
#클래스 메소드 안에 작성할 수 없음
    def hello(self):
        age = 10#  <- age는 hello 메소드의 지역변수(self도 안붙고 cls도 안붙어서)
        self.name = '더조은'
        print(f'{self.name}, 안녕하세요. {age} 살이시네요 ')

print(Car.color) #>> white        #   <- Car 클래스의 객체를 생성하기 전

print(Car()) # >> 0-0--가솔린#       <- Car 클래스의 객체를 생성한 후 
c1 = Car()#      <- c1이라는 변수에 Car 클래스를 적용하고
c1.displacement = 3000#    <- Car 클래스에 있는 함수에 값을 부여함 self.displacement = 0  
c1.door = 4#     <- Car 클래스에 있는 함수에 값을 부여함 self.door = 0  
c1.gear_type = 'auto'#    <- Car 클래스에 있는 함수에 값을 부여함 self.gear_type = ''
print(c1) # >> 3000-4-auto-가솔린#  <- self.fuel 는 별도 지정을 안해서 원래 지정된 값인 가솔린이 나옴

Car.describe()#    <-클래스메소드는 클래스이름으로 접근해서 호출함
# >> describe(cls) 메소드는 Car 클래스의 클래스메소드입니다
print(Car.auto_navi)# >> True

# c1.hello() >> 더조은, 안녕하세요. 10 살이시네요 