# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print(f"이름 : {name}\t 나이 : {age}", end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *lang) :
    print(f"이름 : {name}\t 나이 : {age}\t", end = " ")
    for i in lang :
        print(i, end=" ")
    print()



profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", )