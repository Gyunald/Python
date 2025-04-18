import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from concurrent.futures import ThreadPoolExecutor

def crawl_applyhome_list(year_month=None, region='경기'):
    """아파트 청약 목록을 크롤링하는 함수"""
    
    # 현재 년월 사용 (인자가 없는 경우)
    if year_month is None:
        year_month = datetime.datetime.now().strftime('%Y%m')
    
    # 접속할 URL 및 요청 파라미터 설정
    url = "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.applyhome.co.kr/ai/aia/selectAPTRemndrLttotPblancListView.do",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        "beginPd": year_month,
        "endPd": year_month,
        "suplyAreaCode": region,
        "houseNm": "",
        "chk0": "",
        "pageIndex": "1"
    }
    
    # 결과를 저장할 리스트
    results = []
    
    try:
        # POST 요청 보내기
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # 응답 상태 코드 확인 (4xx, 5xx 에러 발생 시 예외 발생)
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 테이블 데이터 추출
        table = soup.find('table', class_='tbl_st tbl_tb tbl_center tbl_padding mTbl type34')
        
        if table:
            rows = table.find('tbody').find_all('tr')
            
            for row in rows[:2]:
                # 테이블 행의 데이터 속성 추출
                pb_no = row.get('data-pbno')
                hm_no = row.get('data-hmno')
                
                if not pb_no or not hm_no:
                    continue
                
                cols = row.find_all('td')
                if cols and len(cols) >= 9:  # 최소 9개 열이 있는지 확인
                    # 데이터 추출
                    data_row = {
                        '지역': cols[0].text.strip(),
                        '구분': cols[1].text.strip(),
                        '주택명': cols[3].text.strip(),
                        '청약기간': cols[7].text.strip(),
                        '당첨자발표': cols[8].text.strip().split(' ~')[0],
                        '공고번호': pb_no,
                        '주택관리번호': hm_no,
                    }
                    results.append(data_row)
        else:
            print("테이블을 찾을 수 없습니다. 웹사이트 구조가 변경되었을 수 있습니다.")
            
    except requests.RequestException as e:
        print(f"요청 오류 발생: {e}")
    except Exception as e:
        print(f"크롤링 중 오류 발생: {e}")
    
    # 결과 DataFrame으로 변환
    return pd.DataFrame(results)

def get_detail_info(house_manage_no, pblanc_no):
    """주택관리번호와 공고번호를 이용해 상세 정보를 가져오는 함수"""
    
    # 주택 상세 정보 페이지 URL 및 파라미터 설정
    url = "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    params = {
        "houseManageNo": house_manage_no,
        "pblancNo": pblanc_no
    }
    
    detail_info = {}
    
    try:
        # GET 요청 보내기
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. 모집공고문 URL 추출
        for a_tag in soup.find_all('a'):
            if '모집공고문 보기' in a_tag.text:
                detail_info['모집공고문URL'] = a_tag['href']
                break
        
        # 2. 첫 번째 테이블에서 기본 정보 추출
        all_tables = soup.find_all('table')
        if all_tables:
            basic_table = all_tables[0]
            extract_basic_info(basic_table, detail_info)

        # 3. 청약일정 테이블 정보 추출
        extract_schedule_info(soup, detail_info)
        
        # 4. 주택형 및 공급세대수 정보 추출
        extract_house_type_info(soup, detail_info)
        
        # 5. 분양가격 정보 추출
        extract_price_info(soup, detail_info)
        
        # 6. 입주예정월 추출
        extract_move_in_date(soup, detail_info)
            
    except requests.RequestException as e:
        print(f"요청 오류 발생: {e}")
    except Exception as e:
        print(f"상세 정보 가져오기 오류: {e}")

    return detail_info

def extract_basic_info(table, info_dict):
    """기본 정보를 추출하는 함수"""
    rows = table.find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        if len(tds) >= 2:
            label = tds[0].text.strip()
            value = tds[1].text.strip()
            
            if '공급위치' in label:
                info_dict['공급위치'] = value
            elif '공급규모' in label:
                info_dict['공급규모'] = value

def extract_schedule_info(soup, info_dict):
    """청약일정 정보를 추출하는 함수"""
    schedule_heading = soup.find('h5', string=lambda t: t and '청약일정' in t)
    if schedule_heading:
        schedule_table = schedule_heading.find_next('table')
        if schedule_table:
            rows = schedule_table.find_all('tr')
            for row in rows:
                th = row.find('th')
                tds = row.find_all('td')
                
                if not th or not tds:
                    continue
                    
                if '모집공고일' in th.text:
                    info_dict['모집공고일'] = tds[0].text.strip()
                elif '당첨자 발표일' in th.text:
                    announce_text = tds[0].text.strip()
                    if '(' in announce_text:
                        info_dict['당첨자발표상세'] = announce_text.split('(')[0].strip()
                    else:
                        info_dict['당첨자발표상세'] = announce_text
                elif '계약일' in th.text:
                    info_dict['계약일'] = tds[0].text.strip()

def extract_house_type_info(soup, info_dict):
    """주택형 및 공급세대수 정보를 추출하는 함수"""
    house_type_heading = soup.find('h5', string=lambda t: t and '공급대상' in t)
    if house_type_heading:
        house_type_table = house_type_heading.find_next('table')
        if house_type_table:
            house_types = []
            supply_counts = []

            rows = house_type_table.find_all('tr')
            for row in rows:
                # 합계 행은 제외
                if '계' in row.text:
                    continue
                    
                tds = row.find_all('td')
                if not tds:
                    continue
                
                # 첫 번째 행의 경우 (주택구분이 있는 행)
                if '민영' in row.text or '국민' in row.text:
                    if len(tds) >= 6:
                        house_type = tds[1].text.strip()  # 두 번째 열이 주택형
                        supply_count = tds[5].text.strip()  # 여섯 번째 열이 계(총 세대수)
                # 두 번째, 세 번째 행의 경우
                else:
                    if len(tds) >= 5:
                        house_type = tds[0].text.strip()  # 첫 번째 열이 주택형
                        supply_count = tds[4].text.strip()  # 다섯 번째 열이 계(총 세대수)
                
                if house_type and supply_count:
                    house_types.append(house_type)
                    supply_counts.append(supply_count)
            
            if house_types:
                info_dict['주택형'] = ', '.join(house_types)
                info_dict['공급세대수'] = ', '.join(supply_counts)

def extract_price_info(soup, info_dict):
    """분양가격 정보를 추출하는 함수"""
    price_heading = soup.find('h5', string=lambda t: t and '공급금액' in t)
    if price_heading:
        price_table = price_heading.find_next('table')
        if price_table:
            prices = []
            rows = price_table.find_all('tr')
            for row in rows:
                tds = row.find_all('td')
                if len(tds) >= 2:
                    house_type = tds[0].text.strip()
                    price = tds[1].text.strip()
                    if house_type and price:
                        prices.append(f"{house_type}: {price}만원")
            
            if prices:
                info_dict['분양가격'] = ', '.join(prices)

def extract_move_in_date(soup, info_dict):
    """입주예정월 정보를 추출하는 함수"""
    for li in soup.find_all('li'):
        if '입주예정월' in li.text:
            move_in_date = li.text.replace('* 입주예정월', '').replace(':', '').strip()
            info_dict['입주예정월'] = move_in_date
            break

def convert_price_to_billion(price_text):
    """가격을 억 단위로 변환하는 함수"""
    price_text = price_text.replace('만원', '')
    try:
        price_num = float(price_text.replace(',', ''))
        return f"{price_num / 10000:.2f}억"
    except ValueError:
        return price_text

def integrate_house_type_info(item):
    """주택형, 세대수, 가격 정보를 통합하는 함수"""
    if '주택형' not in item or '공급세대수' not in item:
        return
        
    house_types = item['주택형'].split(', ')
    supply_counts = item['공급세대수'].split(', ')
    
    # 가격 정보 추출
    price_info = {}
    if '분양가격' in item:
        price_text = item['분양가격']
        price_items = price_text.split(', ')
        
        for price_item in price_items:
            parts = price_item.split(': ')
            if len(parts) == 2:
                house_type = parts[0].strip()
                price = parts[1].strip()
                price_info[house_type] = price
    
    # 주택형, 세대수, 가격 정보 통합
    if len(house_types) == len(supply_counts):
        house_type_lines = []
        for i in range(len(house_types)):
            house_type = house_types[i]
            supply_count = supply_counts[i]
            
            # 해당 주택형에 대한 가격 정보가 있는지 확인
            price_text = ""
            # 공백 조건 제거하고 모든 주택형에 대해 매칭 시도
            house_type_clean = house_type.strip()
            
            # 정확한 주택형으로 먼저 매칭 시도
            if house_type_clean in price_info:
                price_value = price_info[house_type_clean].replace('만원', '')
                try:
                    price_num = float(price_value.replace(',', ''))
                    price_billion = price_num / 10000
                    price_text = f" ({price_billion:.2f}억)"
                except ValueError:
                    price_text = f" ({price_value})"
            else:
                # 주택형 prefix로 매칭 시도 (예: 059.8001A -> 059)
                for price_type in price_info:
                    # 주택형 번호(숫자 부분)만 추출하여 비교
                    house_prefix = ''.join([c for c in house_type_clean if c.isdigit() or c == '.'])
                    price_prefix = ''.join([c for c in price_type if c.isdigit() or c == '.'])
                    
                    if house_prefix and price_prefix and house_prefix.startswith(price_prefix) or price_prefix.startswith(house_prefix):
                        price_value = price_info[price_type].replace('만원', '')
                        try:
                            price_num = float(price_value.replace(',', ''))
                            price_billion = price_num / 10000
                            price_text = f" ({price_billion:.2f}억)"
                        except ValueError:
                            price_text = f" ({price_value})"
                        break
            
            house_type_lines.append(f"{house_type} : {supply_count}세대{price_text}")
        
        # 주택형 정보 업데이트
        item['주택형'] = '\n'.join(house_type_lines)
    
    # 분양가격 정보는 이미 주택형에 통합했으므로 삭제
    if '분양가격' in item:
        del item['분양가격']
        
def process_single_item(row):
    """단일 항목 처리 함수 (병렬 처리용)"""
    print(f"- {row['주택명']} 상세 정보 수집 중...")
    
    # 기본 정보를 딕셔너리로 변환
    item_data = row.to_dict()
    
    # 상세 정보 수집
    detail_info = get_detail_info(row['주택관리번호'], row['공고번호'])
    
    # 상세 정보를 기본 정보에 통합
    item_data.update(detail_info)
    
    return item_data

def save_as_key_value_txt(data_list, filename):
    """데이터를 지정된 필드 순서로 저장하는 함수"""
    # 지정된 필드 순서
    fields = [
        '주택명', 
        '구분', 
        '청약기간', 
        '당첨자발표', 
        '계약일', 
        '공급위치', 
        '공급규모', 
        '주택형', 
        '분양가격',
        '입주예정일',
        '공고문', 
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        for idx, item in enumerate(data_list):
            # 각 항목을 구분하기 위한 헤더 추가
            f.write(f"#{idx+1}\n")
            
            # URL 필드명 변경
            if '모집공고문URL' in item:
                item['공고문'] = item.pop('모집공고문URL')
            
            # 입주예정월을 입주예정일로 키 변경
            if '입주예정월' in item:
                item['입주예정일'] = item.pop('입주예정월')
            
            # 주택형, 세대수, 가격 정보 통합
            integrate_house_type_info(item)
            
            # 지정된 필드 순서대로 저장
            for field in fields:
                if field in item and item[field]:
                    value = item[field]
                    
                    # 멀티라인 출력이 필요한 필드인지 확인
                    if field == '주택형' and '\n' in value:
                        f.write(f"{field}:\n{value}\n")
                    else:
                        f.write(f"{field}:{value}\n")
            
            # 항목 사이 구분선 추가
            f.write("-" * 30 + "\n")

def main():
    print("아파트 청약 정보 크롤링을 시작합니다...")
    
    # 현재 년월 구하기
    current_ym = datetime.datetime.now().strftime('%Y%m')
    
    # 크롤링 실행
    df_list = crawl_applyhome_list(year_month=current_ym, region='경기')
    
    # 결과 확인
    if not df_list.empty:
        total_items = len(df_list)
        print(f"총 {total_items}개의 목록 데이터를 수집했습니다.")
        
        # 멀티스레딩으로 병렬 처리
        all_data = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            all_data = list(executor.map(process_single_item, [row for _, row in df_list.iterrows()]))
        
        # 지정된 형식으로 텍스트 파일로 저장
        output_filename = f'applyhome_keyvalue_{current_ym}.txt'
        save_as_key_value_txt(all_data, output_filename)
        
        print(f"\n크롤링 완료! 결과 파일: {output_filename} ({len(all_data)}개 항목)")
        
    else:
        print("수집된 데이터가 없습니다. 크롤링 조건을 확인해주세요.")

if __name__ == "__main__":
    main()
