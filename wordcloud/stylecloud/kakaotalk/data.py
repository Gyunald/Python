from wordcloud import WordCloud
from PIL import Image
import numpy as np
import stylecloud

text_a=''
text_b=''
with open("/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/1.txt", "rt", encoding="utf-8",) as f:
    lines_1 = f.readlines()
    for line_1 in lines_1[0:23] :
        if '패패 33' in line_1:
            text_a +=line_1.replace('A','').replace('B','').replace('AB','').replace('O','').replace('운정','').replace('문산','').replace('남','').replace('문산','').replace('ㅋ','').replace('샵검색','').replace('삭제된 메시지입니\n','').replace('삭제된 메시지입니다.\n','').replace('ㅠ\n','').replace('ㅎ\n','').replace('ㅌ\n','').replace('이모티콘\n','').replace('사진\n','').replace('?','').replace('!','')
                  
f = open('/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt', 'wt', encoding="utf-8")
f.writelines(text_a)
f.close()

with open("/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt", "rt", encoding="utf-8",) as f:
    lines_2 = f.readlines()
    for line_2 in lines_2[2:] :
        if '] [' in line_2:
            text_b +=line_2.split(']')[2]

f = open('/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt', 'wt', encoding="utf-8")
f.writelines(text_b)
f.close()

stylecloud.gen_stylecloud(file_path="/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt",
    icon_name="fas fa=poo",
    font_path="/Users/kyu-deokkim/Downloads/D2Coding-Ver1.3.2-20180524/D2Coding/D2Coding-Ver1.3.2-20180524.ttf",
    palette="colorbrewer.diverging.Spectral_11",
    background_color="black",
    gradient="horizontal",
    output_name="패패.png",
    )