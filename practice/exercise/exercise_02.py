# def mysum(*numbers):
#     output = 0
#     for number in numbers :
#         output += number
#     return output
# print(mysum(10,20,30,40))

# def mysum(*numbers):
#     output = 0
#     for number in numbers :
#         output += number
#     return output
# print(mysum(*[1,2,3])) # 리스트 내부의 숫자 더하기


# def mysum(*numbers):
#     output = 0
#     for number in numbers :
#         output += number
#     return output
# print(mysum(*[1,2,3],4))

# def mysum(*numbers):
#     output = 0
#     for number in numbers :
#         output += number
#     output /= len(numbers) # 매개변수로 숫자 리스트를 받고, 평균 구하기
#     return output
# print(mysum(*[1,2,3],4))


# def len_word(*word):
#     li = []
#     count = 0
#     for i in word:
#         li += str(len(i))
#     for j in li:
#         count += int(j) # 문자열로 매개변수로 받고 길이와 평균 구하기
#     print(li)
#     print(min(li))
#     print(max(li))
#     print(count / len(li))
# len_word(*["a","ab","abc","abcd","abcde"])


def len_word(*word):
    output = 0
    for number in word :
        if type(number) == int: # 매개변수가 정수일 경우 더하기
            output += number
        else :
            continue
    print(output)
len_word(*["a",100,"ab","abc",200,"abcd","abcde",300])