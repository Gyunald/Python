import requests
from bs4 import BeautifulSoup

def news_form(title):
    print(f"▶ {title}\n")    
    # print(f"https://land.naver.com/{link}\n")

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_news():
    print("  [증시 헤드라인]")
    print()

    url = "https://finance.naver.com/news/mainnews.naver"
    soup = create_soup(url)

    f = open("news_stock.txt", "w")

    news_1 = soup.find_all(attrs={"class":"articleSubject"})

    f.write("  [증시 헤드라인]"+"\n\n")
    for i in news_1:
        # link = i["href"]
        title = i.get_text().strip()
        f.write(f"▶ {title}"+"\n\n")
        news_form(title)
        # print(index, i.get_text().strip())
        # print(f"https://finance.naver.com/{link}")
    f.close()
if __name__ == "__main__":
    scrape_news()