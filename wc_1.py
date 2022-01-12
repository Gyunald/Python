from konlpy.tag import Okt

with open("/Users/kyu-deokkim/Documents/Git/wordcloud/stylecloud/kakaotalk/11.txt","r") as f:
    text = f.read()

okt = Okt()
nouns = okt.morphs(text)
print(nouns)