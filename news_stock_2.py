import requests
from bs4 import BeautifulSoup
import re

url_list = {
    "액션스퀘어" : "https://search.naver.com/search.naver?where=news&query=%EC%95%A1%EC%85%98%EC%8A%A4%ED%80%98%EC%96%B4&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0", # 액션스퀘어

    "와이제이게임즈" : "https://search.naver.com/search.naver?where=news&query=%EC%99%80%EC%9D%B4%EC%A0%9C%EC%9D%B4%EA%B2%8C%EC%9E%84%EC%A6%88&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0", # 와이제이게임즈

    "주성엔지니어링" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%A3%BC%EC%84%B1%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81&oquery=%EC%99%80%EC%9D%B4%EC%A0%9C%EC%9D%B4%EA%B2%8C%EC%9E%84%EC%A6%88&tqi=hBxg4dprvOsss7PWvqVssssssZ4-468062&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1", # 주성엔지니어링

    "OCI" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%08Oci&oquery=%EC%A3%BC%EC%84%B1%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81&tqi=hBxgClprvmZssnOJaiKssssstVo-030625&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1", # OCI

    "덱스터" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%08%08%EB%8D%B1%EC%8A%A4%ED%84%B0&oquery=%08Oci&tqi=hBxgpdprvOsss7%2FGLGKssssstIs-256767&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1", # 덱스터

    "엠플러스" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%97%A0%ED%94%8C%EB%9F%AC%EC%8A%A4&oquery=%08%08%EB%8D%B1%EC%8A%A4%ED%84%B0&tqi=hBxgVsprvTVssCzngmlssssssUl-081850&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1" # 엠플러스
}

# def news_form(title, link):
#     print(f"▶ {title}")
#     print(f"▶ {link}")

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


li = []
f = open("news_stock_pick.txt", "w", encoding="utf-8")
f.write("  [본전탈출 넘버원]"+"\n\n")
for index, url_name in enumerate(url_list.keys()):
    print(list(url_list.keys())[index])
    # print(index)
    def scrape_news():
        count = 1
        for url in url_list.values():
            if count == 2 :
                continue
            count += 1
            n_url = url
            soup = create_soup(n_url)
            news = soup.find_all(attrs={"class":"news_tit"},limit=2)
              
        for i in news:
            
            title = i["title"]
            link = i["href"]
            print("▶",title)        
            if title in li :
                continue
            else :
                li.append(title)
                f.write(f"▶ {title}"+"\n")
                f.write(f"{link}"+"\n")            

    if __name__ == "__main__":
        scrape_news()
f.close()
    