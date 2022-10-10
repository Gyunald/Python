# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8") # apend
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

# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

import pickle
# profile_file = open("profile.pickle", "wb") # b
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구","골프","코딩"]}
# pickle.dump(profile, profile_file) # profile 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # b
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open ("profile.pickle", "rb") as profile_file :
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
