# -1 은 끝에서부터 시작
# ,는 띄어쓰기 포함
# [ n : n ] 범위 지정 (뒤의 n은 직전까지만 계산) 
jumin = "990120-1234567"

print("성별 :", jumin[7])
print("생년 :", jumin[1:3])
print("월일 :", jumin[2:6])
print("주민번호 :", jumin[7:])
print("주민번호 :", jumin[-7:])

# \n : 줄바꿈
# \" \' : 문장 내에서 따옴표
print("백문이 불여일견\n백견이 불여일타")
print("백문이 '불여일견' \"백견\"이 \'불여일타\'")

# \\ : 문장내에서 \로 인식 (파일경로 \ >>> \\로 변경해야함)
# \r : 커서를 만 앞으로 이동해서 문자열 길이만큼 변경
# print("red apple\rgreen") # green apple이 아니고 greenpple
# \b : 한글자 삭제
# print("red\b apple") 
# \t : 4칸 스페이스
# print("red\tapple") # red    apple



