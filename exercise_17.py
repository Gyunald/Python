from collections import Counter

numbers = [1,2,3,1,2,3,4,1]
s = set()
def how_many_differnt_numbers():
    # c = set(numbers)
    # print(len(c))
    # for i in numbers:
    #     s.add(i)
    # print(len(s))
    # s = {*numbers}
    # print(len(s))
    s.update(numbers)
    print(len(s))

if __name__ == "__main__" :
    how_many_differnt_numbers()