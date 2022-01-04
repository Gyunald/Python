text_a=''
text_b=''
with open("/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/1.txt", "rt", encoding="utf-8",) as f:
    lines = f.readlines()
    for result in lines :
        if "처음" in result[:3] and "@" not in result :
            if len(result) > 10 : # <<< 코드 안먹음
                text_a += result[25:].replace("삭제된 메시지입니다.\n","").replace("사진\n","").replace("이모티콘\n","")
        # text_a +=result.replace('A','').replace('B','').replace('AB','').replace('O','').replace('운정','').replace('문산','').replace('남','').replace('문산','').replace('ㅋ','').replace('샵검색','').replace('삭제된 메시지입니\n','').replace('삭제된 메시지입니다.\n','').replace('ㅠ\n','').replace('ㅎ\n','').replace('ㅌ\n','').replace('이모티콘\n','').replace('사진\n','').replace('?','').replace('!','')
f = open('/Users/kyu-deokkim/Documents/wordcloud/stylecloud/kakaotalk/2.txt', 'wt', encoding="utf-8")
f.writelines(text_a)
f.close()

