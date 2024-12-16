import requests
from bs4 import BeautifulSoup
import time
import re  # 정규 표현식을 사용하기 위해 import
import difflib  # 문자열 유사도 비교를 위해 import

def fetch_news():
    # 네이버 뉴스 페이지 접속
    url = "https://search.naver.com/search.naver?where=news&query=%EC%86%8D%EB%B3%B4&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0"
    response = requests.get(url)
    
    # BeautifulSoup을 사용해 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 뉴스 제목과 링크를 스크랩 (sp_nws1 ~ sp_nws10까지)
    news = []
    for c in range(1, 6):  # sp_nws1부터 sp_nws10까지
        news_item = soup.select(f'#sp_nws{c} > div > div > div.news_contents > a.news_tit')
        if news_item:
            title = news_item[0].get_text()  # 뉴스 제목
            link = news_item[0].get('href')  # 뉴스 링크
            
            # 제목에 정확히 '속보'라는 단어가 포함된 뉴스만 필터링
            if re.search(r'\b속보\b', title):  # '\b'는 단어 경계를 나타냄
                news.append((title, link))
    
    return news

def write_news_to_file(news, filename="news.txt"):
    # 뉴스 제목과 링크를 파일에 기록 (최대 10개 뉴스만 기록)
    with open(filename, 'w', encoding='utf-8') as f:
        for title, link in news[:5]:  # 최대 10개 뉴스만 기록
            f.write(f"{title}\n{link}\n\n")

def read_news_from_file(filename="news.txt"):
    # 기존 뉴스 파일에서 뉴스 읽어오기
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 파일에서 뉴스 제목과 링크를 추출 (2줄씩 묶기)
            news = [(lines[i].strip(), lines[i+1].strip()) for i in range(0, len(lines), 3)]
            return news
    except FileNotFoundError:
        return []  # 파일이 없으면 빈 리스트 반환

def compare_news(previous_news, new_news):
    # 이전 뉴스와 새로운 뉴스 비교하여 새로운 뉴스만 반환
    previous_links = [link for _, link in previous_news]  # 기존 뉴스 링크 추출
    
    # 새로운 뉴스 링크만 필터링
    new_only_news = [(title, link) for title, link in new_news if link not in previous_links]
    
    return new_only_news

def remove_duplicate_titles(new_news):
    # 중복 뉴스 제목 필터링: 유사도가 0.85 이상인 뉴스는 제거
    unique_news = []
    for title, link in new_news:
        # 기존 뉴스와 비교하여 유사한 제목이 있으면 제외
        is_duplicate = False
        for existing_title, _ in unique_news:
            similarity = difflib.SequenceMatcher(None, title, existing_title).ratio()
            if similarity > 0.85:  # 유사도가 85% 이상이면 중복으로 판단
                is_duplicate = True
                break
        if not is_duplicate:
            unique_news.append((title, link))  # 중복이 아니면 리스트에 추가
    return unique_news

def update_news_file(new_news, existing_news, filename="news.txt"):
    # 기존 뉴스에 새로운 뉴스 추가 (최대 10개 뉴스만 기록)
    all_news = new_news + existing_news  # 새로운 뉴스는 맨 앞에 추가
    write_news_to_file(all_news[:5], filename)  # 최신 10개 뉴스만 기록

# 5분마다 반복 실행
while True:
    print("\n[뉴스 스크랩 시작]")
    
    # 1. 최신 뉴스 스크랩
    new_news = fetch_news()

    # 2. 기존 뉴스 파일에서 이전 뉴스 읽어오기
    existing_news = read_news_from_file()

    # 3. 이전 뉴스와 새로운 뉴스 비교하여 새로운 뉴스만 필터링
    new_only_news = compare_news(existing_news, new_news)

    # 4. 중복 뉴스 제거
    new_only_news = remove_duplicate_titles(new_only_news)

    # 5. 새로운 뉴스가 있다면 파일에 기록하고 알림 출력
    if new_only_news:
        # 기존 뉴스에서 오래된 뉴스 삭제하고 새로운 뉴스 추가
        update_news_file(new_only_news, existing_news)
        
        print("새로운 뉴스가 있습니다. 아래 뉴스들이 추가되었습니다:")
        for title, link in new_only_news:
            print(f"제목: {title}\n링크: {link}\n")
    else:
        print("새로운 뉴스가 없습니다.")
    
    # 6. 5분 대기
    print("5분 후 다시 실행합니다...")
    time.sleep(60)  # 5분 대기
