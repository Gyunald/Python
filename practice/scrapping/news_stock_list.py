import requests
from bs4 import BeautifulSoup
f = open("news_stock.list.txt", "w", encoding="utf-8") # 텍스트 파일 생성
f.write("  [본전탈출 넘버원]"+"\n\n") # 텍스트 파일 제목쓰기

search_word = "와이제이게임즈","엘앤에프","후성","맥스트"
for word in search_word :

    url_list = {

        word : f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={word}",
    }

    for url_name in range(1):
        for index_2, url in enumerate(url_list.values()): # 딕셔너리 내 링크 반복
            print()
            f.write(f"▶ {list(url_list.keys())[index_2]}"+"\n\n") # 텍스트 파일 내 종목명 쓰기
            def scrape_news():
                li = [] # 빈 리스트 생성
                cnt = 0 # 인덱스 생성
                headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
                res = requests.get(url, headers = headers)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, "lxml")
                news = soup.find_all(attrs={"class":"news_tit"},limit=3) # 태그 내 클래스 속성이 news_tit , 기사 3개씩 크롤링
                print(f"▶ {list(url_list.keys())[index_2]}\n") # 종목 출력
                
                # print(f"{link}")
                for i in news: # 반복
                    title = i["title"] # 태그 내 제목 속성
                    link = i["href"] # 태그 내 링크 속성
                    if title in li : # 리스트 내 같은 제목 있으면 거르기
                        continue
                    else :
                        li.append(title) # 리스트에 제목 추가
                        f.write(f"◈ {title}"+"\n") # 텍스트 파일에 제목 쓰기
                        f.write(f"  {link}"+"\n\n") # #텍스트 파일에 링크 쓰기
                        print(f"◈ {li[cnt]}") # 리스트 내 제목 출력
                        cnt += 1 # 리스트 내 인덱스 1씩 이동
            if __name__ == "__main__" :
                scrape_news() # 함수 실행
f.close() # 쓰기 종료