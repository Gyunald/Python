# day = randint(4,28)
# day_off = "1~3"

# print(f"오프라인 스터디 모임 날짜는 매월 {day}일로 선정 되었습니다.")
# print(f"매월 {day_off}일은 스터디 준비를 해야하는 날입니다.")

# http://naver.com -> nav51!
# 규칙1 : http:// 지우기
# 규칙2 : .이후 지우기
# 규칙3 : 처음 세자리 + 글자 갯수 + 'e'의 갯수 + "!" 로 구성


# a = "http://daum.net"
# b = a.replace("http://","")
# c = b[:b.index(".")]
# print(f"비밀번호는 {c[0:3]}{len(c)}{c.count('e')}! 입니다.")

# ulr = "http://naver.com"
# a = ulr.replace("http://","")
# b = a[0:a.index(".")]
# password = b[0:3]+str(len(b))+str(b.count("e"))+"!"
# print(f"""
# {ulr}
# 비밀번호는 {password} 입니다.
# """)


station = ["사당", "신도림", "인천공항"]
print(f"{station[1]}행 열차가 들어오고 있습니다.")

station = ["사당", "신도림", "인천공항"]
for i in station :
    print(f"{i}행 열차가 들어오고 있습니다.")