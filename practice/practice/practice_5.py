# abs 절대값 pow 제곱 max 최댓값 min 최솟값 round 반올림 
# floor 내림 ceil 올림 sqrt 제곱근

# print("A","B","C", sep=",", end=" ")
# print("123456")

# import sys
# print("A","B","C", file = sys.stdout)
# print("A","B","C", file = sys.stderr)

# scores = {"a":0, "b":50, "c":100}
# for subject, score in scores.items() :
#     print(subject.ljust(4), str(score).rjust(4),sep=":")

# 대기 순번표
# 001, 002, 003, ...
# for num in range(20+1) :
#     print("대기번호 : " + str(num).zfill(3))

# 표준 입력
# answer = input("아무값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신값은" + answer + "입니다")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 부호 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽정렬,빈칸 _
print("{0:_<10}".format(500))
# 3자리 마다 콤마
print("{0:,}".format(500000000000))
# 3자리 마다 콤마와 부호
print("{0:+,}".format(500000000000))
print("{0:+,}".format(-500000000000))
# 3자리 마다 콤마(,)와 부호(+)와 자릿수(30) 확보
# 빈 자리는 ^ 로 채우기
print("{0:^<+30,}".format(500000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 자릿수 지정 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))