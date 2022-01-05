from typing import Counter
from konlpy.tag import Okt
import re
import stylecloud

with open("/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/1.txt", "rt", encoding="utf-8",) as f:
    text = f.read()

text_a = text.replace(" ","")

text_b=[]

for text_c in text_a.split():
    if len(text_c) > 2 : # 출력할 단어의 길이 지정
        text_b.append(text_c.strip(".,"))

f = open('/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt', 'wt', encoding="utf-8")
f.writelines(text_b)
f.close()

count = Counter(text_b)
count_list = count.most_common(10)
print(count_list())

stylecloud.gen_stylecloud(file_path='/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt',
    icon_name="fas fa=poo",
    font_path="/Users/kyu-deokkim/Downloads/D2Coding-Ver1.3.2-20180524/D2Coding/D2Coding-Ver1.3.2-20180524.ttf",
    palette="colorbrewer.diverging.Spectral_11",
    background_color="black",
    gradient="horizontal",
    output_name="패패.png",
    )
