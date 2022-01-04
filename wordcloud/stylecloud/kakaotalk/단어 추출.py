from konlpy.tag import Okt
import re

with open("/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt", "rt", encoding="utf-8",) as f:
    text = f.read()


text_a = text.replace(" ","")

text_b=[]

for text_c in text_a.split():
    if len(text_c) > 10 : # 출력할 단어의 최소길이 지정
        text_b.append(text_c.strip(".,"))

words_cnt = []
i = 0
for words in set(text_b):
    words_cnt.append((words,text_b.count(words)))
#     i += 1  #디버깅용
#     if i ==100 :break
print(words_cnt)

words_cnt.sort(key = lambda x:x[1], reverse = True) #튜플의 1인덱스(count) 기반으로 sort함
words_cnt[:15]
