kospi_top10 = ['삼성전자','sk하이닉스','현대차','한국전력','아모레퍼시픽','제일모직','삼성전자우','삼성생명','naver','현대모비스']
print(kospi_top10)
kospi_top10.insert(3,'sk텔레콤')
print('len =',len(kospi_top10))
print('kospi_top11[-1] =', kospi_top10[-1])
del kospi_top10[-1]
print('len =',len(kospi_top10))
print(kospi_top10)
