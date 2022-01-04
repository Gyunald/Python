# 파일 쓰기 
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0","\n영어 : 50", "\n국어 : 100", end="", file=score_file)

# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("\n과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end ="")
# score_file.close()

# 몇 줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf-8")
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="")
# score_file.close()

# list 형태로 저장

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() 
for line in lines :
    print(line, end="")
score_file.close()