# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="\n")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# while 1 :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()