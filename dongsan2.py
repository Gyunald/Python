import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 대상 URL
URL = "https://www.aptrank.com/apt_js_recent_detail.php?pagenum=1&addcode=41480&pgroup=30&buildperiod="

# HTTP 요청 헤더 설정
HEADERS = {"User-Agent": "Mozilla/5.0"}

try:
    # HTTP GET 요청 보내기
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()  # 요청 오류 발생 시 예외 발생
except requests.RequestException as e:
    print(f"HTTP 요청 중 오류 발생: {e}")
    exit()

try:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 테이블 요소 선택
    table = soup.select_one("body > div:nth-child(3) > table")
    if not table:
        print("테이블을 찾을 수 없습니다.")
        exit()

    # 테이블의 행 데이터 가져오기
    rows = table.find_all("tr")
    raw_data = []

    for row in rows:
        columns = row.find_all("td")
        row_data = [col.get_text(strip=True) for col in columns]
        if row_data:  # 빈 데이터 제외
            raw_data.append(row_data)
except Exception as e:
    print(f"HTML 파싱 중 오류 발생: {e}")
    exit()

# 데이터 파일로 저장
output_file = "dongsan2.txt"
try:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"{datetime.today().date()}\n파주시 전세가 상위\n\n")
        for row in raw_data[1:]:  # 첫 번째 행은 헤더로 간주
            try:
                # 데이터 처리 및 파일 쓰기
                단지명 = row[1].split('경기도')[0].replace('신도시', '').replace('아파트', '').replace('단지', '').replace('마을', '')
                위치 = row[1].split('파주시')[1]
                계약일 = row[3]
                면적 = row[4]
                층수 = row[5]
                거래금액 = row[6]
                if float(면적.split('㎡')[0]) > 90 :
                    continue

                file.write(f"{단지명} {거래금액}\n")
                file.write(f"{위치} {층수} {면적}\n")
                file.write(f"계약일: {계약일}\n\n")
            except IndexError:
                print(f"데이터 처리 중 오류 발생: {row}")
except IOError as e:
    print(f"파일 저장 중 오류 발생: {e}")
    exit()

print(f"데이터가 '{output_file}' 파일에 저장되었습니다.")
