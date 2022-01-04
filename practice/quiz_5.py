for i in range(1,5) :
    with open(f"{i}주차.txt", "w", encoding="utf-8") as a :
        a.write(f"- {i}주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :")
print(a)