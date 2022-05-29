from wordcloud import WordCloud
from PIL import Image
import numpy as np
import stylecloud
import csv


def rep():
    for j in c:
        return i[26:].replace(j,"").replace('"',"").replace(c[0],"").replace(c[1],"").replace(c[2],"").replace(c[-1],"")

c = ["이모티콘","사진","삭제된 메시지입니다","ㅋ"]

with open("/Users/kyu-deokkim/Downloads/2.csv", "rt", encoding="utf-8") as r, open("/Users/kyu-deokkim/Downloads/3.txt", "wt", encoding="utf-8") as w:
    for i in r.readlines():
        if "찐쥬린" in i:
            w.writelines(rep())

w.close()

stylecloud.gen_stylecloud(file_path="/Users/kyu-deokkim/Downloads/3.txt",
    icon_name="fas fa=cloud",
    font_path="/Users/kyu-deokkim/Downloads/D2Coding-Ver1.3.2-20180524/D2Coding/D2Coding-Ver1.3.2-20180524.ttf",
    palette="colorbrewer.diverging.Spectral_11",
    background_color="black",
    gradient="horizontal",
    output_name="2.png")
