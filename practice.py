# abs 절대값 pow 제곱 max 최댓값 min 최솟값 round 반올림 
# floor 내림 ceil 올림 sqrt 제곱근

# scores = {"a" : 0, "b" : 50, "c" : 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# # zfill(n) n만큼 0으로 처리 3 = 001, 2 = 01
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬, 10자리
print(f"{500: >10}")

# 양수일땐 + , 음수일 땐 -
print(f"{500: >+10}")
print(f"{-500: >+10}")

# 왼쪽 정렬, 빈칸은 _
print(f"{500:_<10}")

# 3자리 마다 콤마
print(f"{500000000000:+,}")
print(f"{-500000000000:+,}")

# 빈 자리는 ^, 왼쪽정렬, 부호, 자릿수 확보, 3자리 마다 콤마
print(f"{500000000000:^<+30,}")

# 소수점 출력 (2째 자리에서 반올림)
print(f"{5/3:.2f}")