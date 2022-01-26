for i in range(1,4) :
    with open(f"{i}주차.txt", "w", encoding="utf-8") as f:
        f.write(f"""- {i} 주차 주간보고 -
        
부서 :
이름 :
업무 요약 :
""")