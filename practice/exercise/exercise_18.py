# def wordcount():   
#     counts = {
#         "characters" : 0,
#         "words" : 0,
#         "lines" : 0,
#     }
#     unique_words = set()

#     for one_line in f:
#         counts["characters"] += len(one_line)
#         counts["words"] += len(one_line.split())
#         counts["lines"] += 1
#         unique_words.update(one_line.split())
#     counts["unique_words"] = len(unique_words)

#     for key,value in counts.items():
#         print(f"{key} : {value}")

# f = open("/Users/kyu-deokkim/Documents/Git/practice/news_land.txt", "r",)

# if __name__ == "__main__" :
#     wordcount()

def wordcount():
    a = input("단어입력 >>> ")
    word = {a : 0}
    for i in f:
        if a in i:
            word[a] += len(a.split())

    for key,value in word.items():
        print(f"{key} : {value}")

f = open("/Users/kyu-deokkim/Documents/Git/practice/news_land.txt", "r",)

if __name__ == "__main__" :
    wordcount()