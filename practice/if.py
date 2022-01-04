# wearther = input("날씨가 어때요?")

# if wearther == "비" or wearther == "눈" :
#     print("우산")
# elif wearther == "맑음" :
#     print("모자")
# else :
#     print("걍고")

temp = int(input("기온이 어때요?"))
if 30 <= temp :
    print("더워요")
elif 10 <= temp < 30 :
    print("좋아요")
elif 0 <= temp < 10 :
    print("추워요")
else :
    print("나가지 마세요")