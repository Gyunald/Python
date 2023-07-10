from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import streamlit as st
import pandas as pd
from datetime import time

def generate_work_schedule(start_time, end_time):
    schedule = []

    breaks = [start_time,'10:00', '10:10', '12:00', '13:00', '15:00', '15:10', '17:00', '17:20',end_time]
    breaks = sorted(list(set(breaks)))
    try:
        for i in range(len(breaks) - 1):
            if start_time <= breaks[i] < end_time:
                if breaks[i] == '12:00' or breaks[i] == '17:00':
                    continue
                if start_time < breaks[i+1] :
                    schedule.append({'시작시간': breaks[i], '종료시간': breaks[i + 1]})

        if len(schedule) == 0 or schedule[0]['종료시간'] <= schedule[0]['시작시간']:
            schedule = [{'시작시간': start_time, '종료시간': end_time}]

        return schedule
    except:
        return None

c1,c2,c3 = st.columns(3)

with c1 :
    name = st.selectbox('이름',['김규덕','김진석'])
    id =st.text_input('ID','kdkim') 
    pw = st.text_input("PASSWORD",value='xjsld12#',type='password')
    
with c2 :
    so = st.text_input('샵오더') 
    work = st.text_input('상세내용')
    etc = st.text_input('비고')

c4,c5,c6 = st.columns(3)

with c4: 
    e = st.empty()
    e2 = st.empty()
    start_time = e.time_input('시작 시간1')
    end_time = e.time_input('종료 시간1')
    e.empty()

with c5 :
    start_time = st.time_input('시작 시간',time(8,0),key='s',step=600).strftime('%H:%M')
    end_time = st.time_input('종료 시간',time(17,0),key='e',step=600).strftime('%H:%M')
        # 유효성 검사
    if start_time >= end_time:
        st.error('종료 시간은 시작 시간보다 이후여야 합니다.')
    else:
        # 근무시간표 생성
        schedule = generate_work_schedule(start_time, end_time)

        # 결과 출력
        if schedule is not None:
            # 데이터프레임 생성
            df = pd.DataFrame(schedule)
            # 시작시간이 입력된 경우 추가
            if start_time not in df['시작시간'].values:
                new_row = {'시작시간': start_time, '종료시간': df.iloc[0]['시작시간']}
                df = pd.concat([pd.DataFrame([new_row]), df], ignore_index=True)
        else:
            st.error('시간 확인')

    timetable = generate_work_schedule(start_time, end_time)
    e2.dataframe(schedule)
    f = st.checkbox('가공완료')
    run = st.button('등록',use_container_width=True)

if run :    
    chrome_optiins = Options() # 브라우저 꺼짐 방지
    chrome_optiins.add_experimental_option('detach', True)
    chrome_optiins.add_experimental_option('excludeSwitches', ['enable-logging']) # 불필요한 에러 메세지 삭제
    service = Service(executable_path=ChromeDriverManager().install()) # 크롬 드라이버 최신 버전 자동 설치 후 서비스 만들기
        
    #URL 얻기
    driver = webdriver.Chrome(service=service,options= chrome_optiins)

    # 크롬 브라우저 사이즈
    driver.set_window_size(1400, 1000)
    # 주소 이동
    driver.get('https://emes.imi-critical.com/imi_clive/')

    driver.find_element(By.NAME, 'log_id').send_keys(id)
    driver.find_element(By.NAME, 'passwd').send_keys(pw)
    driver.find_element(By.XPATH, '//*[@id="btLogin"]').click()
    # 5초 까지 대기
    driver.implicitly_wait(5)

    # 현재창 인식
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="frMain"]'))

    # 작업일보 이동
    driver.find_element(By.XPATH, '//*[@id="div_main_menu"]/ul[1]/li[4]/a').click()
    driver.find_element(By.XPATH, '//*[@id="div_main_menu"]/ul[1]/li[4]/ul/li[4]/a').click()

    # 5초 까지 대기
    driver.implicitly_wait(5)

    # 작업일보 작성
    driver.find_element(By.XPATH, '//*[@id="div_top"]/div[1]/button[2]').click()

    # 5초 까지 대기
    driver.implicitly_wait(5)

    # 팀선택
    driver.find_element(By.XPATH, '//*[@id="div_pop_result"]/div[2]/table/tbody/tr/td[2]/select').click()
    driver.find_element(By.XPATH, '//*[@id="div_pop_result"]/div[2]/table/tbody/tr/td[2]/select/option[4]').click()

    # 작업자선택
    driver.find_element(By.XPATH, f"//select[@name='s_WR_Worker']/option[text()='{name}']").click()

    for i in range(1,len(timetable)+1):
        if timetable[i-1]['시작시간'] == '10:00' or timetable[i-1]['시작시간'] == '15:00':
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/select/option[9]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/input').send_keys('휴식')
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[4]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/input[1]').send_keys(timetable[i-1]['시작시간'])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[8]/input[1]').send_keys(timetable[i-1]['종료시간'])
            continue

        elif so == '' or etc != '':
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/select/option[9]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/input').send_keys(work)
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[13]/input').send_keys(etc)
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[4]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/input[1]').send_keys(timetable[i-1]['시작시간'])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[8]/input[1]').send_keys(timetable[i-1]['종료시간'])
            continue
        
        # 샵오더 
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[10]/input').send_keys(so)
        # # 수량
        # driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[12]/input').send_keys(수량)

        # 작업명
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/select/option[11]').click()

        # 상세내용        
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/input').send_keys(work)

        # 작업코드
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[3]').click()
    
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/input[1]').send_keys(timetable[i-1]['시작시간'])
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[8]/input[1]').send_keys(timetable[i-1]['종료시간'])
        
        # OP No
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[11]/select/option[3]').click()
