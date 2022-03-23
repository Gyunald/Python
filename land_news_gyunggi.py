from operator import index
import requests
from bs4 import BeautifulSoup
import re

def news_form(index, title, link):
    print(f"{index + 1}." , title)
    print(f"https://land.naver.com/{link}\n")

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_news():
    print("[부동산 헤드라인 - 경기도]")
    url = "https://land.naver.com/news/region.naver"
    soup = create_soup(url)

    news_1 = soup.find("ul", attrs={"class":"headline_list live_list NEI=a:lst.title"}).find_all("li")


    for index, i in enumerate(news_1):
        title_index_1 = 0
        img_1 = i.find("img")
        if img_1:
            title_index_1 = 1 # 이미지가 없으면 0번째, 이미지가 있으면 1번째 
            
        img_title_1 = i.find_all("a")[title_index_1]
        title = img_title_1.get_text().strip()
        link = img_title_1["href"]
        news_form(index, title, link)

    # with open("land_news_region.txt", "w", encoding="utf-8") as f:
    #     f.write()

if __name__ == "__main__":
    scrape_news()