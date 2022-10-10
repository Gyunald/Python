import requests
from bs4 import BeautifulSoup
import re

# res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4")
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# images = soup.find_all("img", attrs={"onerror":"this.src='https://ssl.pstatic.net/sstatic/keypage/outside/scui/weboriginal_new/im/no_img.png'"})

# for idx, image in enumerate(images):
#     site = image["src"]
#     image_res = requests.get(site)
#     image_res.raise_for_status()
#     if idx >= 3 :
#         break
#     with open(f"movie{idx + 1}.png", "wb") as f:
#         f.write(image_res.content)
#         print(f"{idx+1}위", image["alt"])


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def news_form(index, title, link):
    print(f"{index + 1}." , title)
    print(f"{link}")   


# 날씨 정보

def scrape_weather():
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8F%99%ED%8C%A8%EB%8F%99++%EB%82%A0%EC%94%A8&oquery=%EB%AC%B8%EC%82%B0++%EB%82%A0%EC%94%A8&tqi=hBEXKlp0YihssedgTrwssssstX8-514277"
    soup = create_soup(url)

    weather = soup.find("p", attrs={"class":"summary"}).get_text()
    weather_2 = soup.find("div", attrs={"class":"weather_graphic"}).get_text()
    weather_3 = soup.find("ul", attrs={"class":"today_chart_list"}).get_text()
    weather_4 = soup.find("dl", attrs={"class":"summary_list"}).get_text()
    print("[동패동 날씨]")
    print(weather.strip())
    print(weather_2.strip())
    print(weather_3.strip())
    print(weather_4.strip())
    print()


# 헤드라인 뉴스 #
# def scrape_news():
#     print("[헤드라인 뉴스]")
#     url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=260"
#     soup = create_soup(url)

#     news = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li",limit=5)
    
#     for index, i in enumerate(news):
#         title = i.find("img")["alt"]
#         link = i.find("img")["src"]
#         news(index, title, link)

def scrape_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=260"
    soup = create_soup(url)

    news = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li",limit=5)
    
    for index, i in enumerate(news):
        title_index = 0
        img = i.find("img")
        if img:
            title_index = 1 # 이미지가 없으면 0번째, 이미지가 있으면 1번째 
            
        img_title = i.find_all("a")[title_index]
        title = img_title.get_text().strip()
        link = img_title["href"]
        news_form(index, title, link)
        print()

def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)

    english = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    today_expression = soup.find_all("b", attrs={"class":"conv_txtTitle"})

    print("(영어 지문)")
    print(f"오늘의 표현 : {today_expression[1].get_text()}")
    print()
    for i in english[len(english) // 2:]:
        print(i.get_text().strip())        
    print()
    print("(한글 지문)")
    print(f"오늘의 표현 : {today_expression[0].get_text()}")
    print()
    for j in english[:len(english) // 2]:
        print(j.get_text().strip())
    print()


if __name__ == "__main__":
    scrape_weather()
    scrape_news()
    scrape_english()
    