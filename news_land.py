import requests
from bs4 import BeautifulSoup
import re

def news_form_1(title, link):
    print(f"▶ {title}")
    print(f"https://land.naver.com{link}\n")

def news_form_2(title, link):
    print(f"▶ {title}")
    print(f"https://land.naver.com/{link}")

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_news():
    print("[부동산 헤드라인]")
    print()
    url = "https://land.naver.com/news/headline.naver"
    soup = create_soup(url)

    news_1 = soup.find("div", attrs={"class":"news_area NE=a:hla"}).find_all("dt",limit=2)
    news_2 = soup.find("ul", attrs={"class":"headline_list"}).find_all("li")

    f = open("news_land.txt", "w")
    f.write("  [부동산 헤드라인]"+"\n\n")

    for i in news_1:
        title_index_1 = 0
        img_1 = i.find("img")
        if img_1:
            title_index_1 = 1 # 이미지가 없으면 0번째, 이미지가 있으면 1번째 
            
        img_title_1 = i.find_all("a")[title_index_1]
        title = img_title_1.get_text().strip()
        link = img_title_1["href"]
        f.write(f"▶ {title}"+"\n")
        f.write(f"  https://land.naver.com{link}"+"\n\n")
        news_form_1(title, link)

    for j in news_2:
        title_index_2 = 0
        img = j.find("img")
        if img:
            title_index_2 = 1
            
        img_title = j.find_all("a")[title_index_2]
        title = img_title.get_text().strip()
        link = img_title["href"]
        f.write(f"▶ {title}"+"\n")
        f.write(f"  https://land.naver.com{link}"+"\n\n")
        news_form_2(title, link)
        print()
    f.close()
if __name__ == "__main__":
    scrape_news()