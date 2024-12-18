
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure ChromeDriver
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--enable-unsafe-swiftshader')

# Initialize WebDriver
browser = webdriver.Chrome(options=chrome_options)

# Load the webpage
url = "https://www.todayoung.com/apart/load_apart.html?area_code=4148000000&stype=new"  # Update with your file path
browser.get(url)

# Find all matching elements with specific onclick pattern
list_items = browser.find_elements(By.XPATH, "//li[contains(@onclick, '4148000000&apt')]")

# Extract and print the required details
c=0
l = []

for item in list_items:
    
    # Apartment name
    name = item.find_element(By.XPATH, ".//h6").text.split('\u00a0')[0]

    # Location, floor, size, and contract date
    details = item.find_element(By.XPATH, ".//span[contains(@class, 'text-xs')]").text

    # Price
    price = item.find_element(By.XPATH, ".//div[contains(@class, 'font-weight-bold')]").text #.replace('.0억', '억')

    l.append(f"{name.replace(' NEW', '').replace('마을','').replace('단지','').replace('아파트','')} {price}\n{details.replace('·',' ').replace('m2','㎡')}\n")
    c+=1
# Close the browser
browser.quit()

output_file = "dongsan1.txt"

try:
    with open('dongsan.txt1', 'w', encoding='utf-8') as file:
        file.write(f"{datetime.today().date()}\n파주시 실거래 {c}건\n\n")
        for item in l:
            file.write(item + '\n')  # 각 요소를 한 줄씩 작성
except Exception as e:
    file.write(f"Error processing item: {e}\n")

print(f"데이터가 '{output_file}' 파일에 저장되었습니다.")
