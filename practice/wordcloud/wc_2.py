from matplotlib import colors
from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("/Users/kyu-deokkim/Documents/Git/wordcloud/stylecloud/kakaotalk/11.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines :
        text += line

font = "/Users/kyu-deokkim/Downloads/나눔 글꼴/나눔명조/NanumFontSetup_TTF_MYUNGJO/NanumMyeongjo.ttf"

wc = WordCloud(font_path=font,background_color="white", width=500,height=500,min_font_size=20)
wc.generate(text)
wc.to_file("result.png")
