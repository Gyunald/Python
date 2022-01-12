import warnings
import konlpy
from konlpy.corpus import kolaw
from konlpy.corpus import kobill
from konlpy.tag import *
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from nltk import Text
from wordcloud import WordCloud

print("\n ## konlpy 버전확인 ## \n", konlpy.__version__)

c = kolaw.open('constitution.txt').read()

print("\n ## 대상 데이터확인 ## \n", c[:40])

print(kolaw.fileids())

d = kobill.open('1809890.txt').read()

print("\n ## 대상 데이터확인(상세) ## \n", d[:40])

print(kobill.fileids())

""" KoNLPy 다양한 형태소 분석, 태깅 라이브러리

    Hannanum: 한나눔. KAIST Semantic Web Research Center 개발.

    http://semanticweb.kaist.ac.kr/hannanum/

    Kkma: 꼬꼬마. 서울대학교 IDS(Intelligent Data Systems) 연구실 개발.

    http://kkma.snu.ac.kr/

    Komoran: 코모란. Shineware에서 개발.

    https://github.com/shin285/KOMORAN

    Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.

    https://github.com/open-korean-text/open-korean-text """

hannanum = Hannanum()

kkma = Kkma()

komoran = Komoran()

okt = Okt()

print("\n ## 명사 추출(hannanum) ## \n", hannanum.nouns(c[:40]))

print("\n ## 명사 추출(kkma) ## \n", kkma.nouns(c[:40]))

print("\n ## 명사 추출(Komoran) ## \n", komoran.nouns("\n".join([s for s in c[:40].split("\n") if s])))

print("\n ## 명사 추출(okt) ## \n", okt.nouns(c[:40]))


print("\n ## 형태소 추출(hannanum) ## \n", hannanum.morphs(c[:40]))

print("\n ## 형태소 추출(kkma) ## \n", kkma.morphs(c[:40]))

print("\n ## 형태소 추출(Komoran) ## \n", komoran.morphs("\n".join([s for s in c[:40].split("\n") if s])))

print("\n ## 형태소 추출(okt) ## \n", okt.morphs(c[:40]))

print("\n ## 품사 부착(hannanum) ## \n", hannanum.pos(c[:40]))

print("\n ## 품사 부착(kkma) ## \n", kkma.pos(c[:40]))

print("\n ## 품사 부착(Komoran) ## \n", komoran.pos("\n".join([s for s in c[:40].split("\n") if s])))

print("\n ## 품사 부착(okt) ## \n", okt.pos(c[:40]))

print("\n ## 품사 태그의 기호와 의미(okt) ## \n", okt.tagset)

tagsets = pd.DataFrame()

N = 67

tagsets["Hannanum-기호"] = list(hannanum.tagset.keys()) + list("*" * (N - len(hannanum.tagset)))

tagsets["Hannanum-품사"] = list(hannanum.tagset.values()) + list("*" * (N - len(hannanum.tagset)))

tagsets["Kkma-기호"] = list(kkma.tagset.keys()) + list("*" * (N - len(kkma.tagset)))

tagsets["Kkma-품사"] = list(kkma.tagset.values()) + list("*" * (N - len(kkma.tagset)))

tagsets["Komoran-기호"] = list(komoran.tagset.keys()) + list("*" * (N - len(komoran.tagset)))

tagsets["Komoran-품사"] = list(komoran.tagset.values()) + list("*" * (N - len(komoran.tagset)))

tagsets["OKT-기호"] = list(okt.tagset.keys()) + list("*" * (N - len(okt.tagset)))

tagsets["OKT-품사"] = list(okt.tagset.values()) + list("*" * (N - len(okt.tagset)))

print("\n ## 품사 태그의 기호와 의미 ## \n", tagsets)