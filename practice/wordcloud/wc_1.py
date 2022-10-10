from wordcloud import WordCloud
from PIL import Image
import numpy as np
import stylecloud
import csv

def rep(i):
    for j in c:
        for j in c:
            if j in i:
                return
        else: 
            return w.writelines(i[l:].replace('"',""))
            # return w.writelines(i[l:].replace('"',""))

name = "스윙중짜/창원/31"
l = 23+len(name)
c = f"{name}님","샵검색","이모티콘","사진","삭제된 메시지입니다","ㅋ","https","ㅎ"

with open("/Users/kyu-deokkim/Downloads/2.csv", "rt", encoding="utf-8") as r, open("/Users/kyu-deokkim/Downloads/3.txt", "wt", encoding="utf-8") as w:
    [rep(i) for i in r.readlines() if name in i]
    
    
w.close()

stylecloud.gen_stylecloud(file_path="/Users/kyu-deokkim/Downloads/3.txt",
    icon_name="fas fa=cloud",
    font_path="/Users/kyu-deokkim/Downloads/D2Coding-Ver1.3.2-20180524/D2Coding/D2Coding-Ver1.3.2-20180524.ttf",
    palette="colorbrewer.diverging.Spectral_11",
    background_color="black",
    gradient="horizontal",
    output_name="2.png")
