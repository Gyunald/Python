from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import streamlit as st
import pandas as pd
from datetime import time, datetime, timedelta

# prompt = st.chat_input("Say something")

if "messages" not in st.session_state:
    st.session_state.messages = []
if 'direct' not in st.session_state:
    st.session_state.direct = []
if 'indirect' not in st.session_state:
    st.session_state.indirect = []



def direct_schedule(start_time, end_time):
    schedule = st.session_state.direct

    breaks = [start_time,'10:00', '10:10', '11:45', '12:45', '15:00', '15:10', '17:00', '17:20',end_time]
    breaks = sorted(list(set(breaks)))
    try:
        if start_time < end_time:
            for i in range(len(breaks) - 1):
                if start_time <= breaks[i] < end_time:
                    if breaks[i] == '11:45' or breaks[i] == '17:00':
                        continue
                    if start_time < breaks[i+1] :
                        schedule.append({'시작시간': breaks[i], '종료시간': breaks[i + 1]})

            if len(schedule) == 0 or schedule[0]['종료시간'] <= schedule[0]['시작시간']:
                schedule = [{'시작시간': start_time, '종료시간': end_time}]

            return schedule
            
        else:
            e.error('시간 확인')  
        
    except:
        return None

def indirect_schedule(start_time2, end_time2):
    schedule2 = st.session_state.indirect
    breaks = [start_time2,'10:00', '10:10', '11:45', '12:45', '15:00', '15:10', '17:00', '17:20',end_time2]
    breaks = sorted(list(set(breaks)))
    try:
        if start_time2 < end_time2:
            for i in range(len(breaks) - 1):
                if start_time2 <= breaks[i] < end_time2:
                    if breaks[i] == '11:45' or breaks[i] == '17:00':
                        continue
                    if start_time2 < breaks[i+1] :
                        schedule2.append({'시작시간': breaks[i], '종료시간': breaks[i + 1]})

            if len(schedule2) == 0 or schedule2[0]['종료시간'] <= schedule2[0]['시작시간']:
                schedule2 = [{'시작시간': start_time2, '종료시간': end_time2}]

            return schedule2
            
        else:
            e.error('시간 확인')
        
    except:
        return None

c1,c2,c3 = st.columns(3)

with c1 :
    name = st.selectbox('이름',['김규덕','김진석'])
    so = st.text_input('샵오더') 
    work = st.text_input('상세내용')
    id ='kdkim'
    pw = 'xjsld12#'
    
with c2 :
    start_time = st.time_input('시작 시간',time(8,0),step=600).strftime('%H:%M')
    end_time = st.time_input('종료 시간',time(20,20),step=600).strftime('%H:%M')    
    finish = st.checkbox('가공완료')
    indirect_chech = st.checkbox('간접작업')

    # etc = st.text_input('비고')

c4,c5,c6 = st.columns(3)

with c4: 
    e = st.empty()
    # start_time = e.time_input('시작 시간',key='s1').strftime('%H:%M')
    # end_time = e.time_input('종료 시간',key='e1').strftime('%H:%M')
    e.empty()

with c5 :
    if indirect_chech :
        e2 = st.empty()
        indirect = e2.selectbox('간접작업',['타운홀미팅','직무교육','기타'])
        start_time2 = st.time_input('간접작업 시작',time(14,20), step=600).strftime('%H:%M')
        end_time2 = st.time_input('간접작업 종료',time(15,20), step=600).strftime('%H:%M')
        run_indirect = st.button('등록',use_container_width=True,key='b1')
        if indirect == '기타':
            e2.text_input('기타')

        if run_indirect :          
            st.session_state.direct.clear()  
            st.session_state.indirect.clear()
            timetable = direct_schedule(start_time, end_time)
            timetable2 = indirect_schedule(start_time2,end_time2)
            df = pd.DataFrame(timetable+timetable2).drop_duplicates()
            df = df.sort_values(['시작시간', '종료시간']).reset_index(drop=True)
            for i in range(1, len(df)):
                if df.loc[i-1, '종료시간'] > df.loc[i, '시작시간'] and df.loc[i-1,'시작시간'] != df.loc[i,'시작시간']:
                    df.loc[i-1, '종료시간'] = df.loc[i, '시작시간']

                elif df.loc[i-1, '종료시간'] > df.loc[i, '시작시간'] and df.loc[i-1,'시작시간'] == df.loc[i,'시작시간']:
                    df.loc[i, '시작시간'] = df.loc[i-1, '종료시간']
            with c4:
                st.dataframe(df)
    else:        
        run_direct = st.button('등록',use_container_width=True,key='b2')

        if run_direct :
            st.session_state.direct.clear()
            with c4:
                timetable = direct_schedule(start_time, end_time)
                df = pd.DataFrame(timetable)
                st.dataframe(df)
st.session_state.direct
st.session_state.indirect

# if run :    
#     chrome_optiins = Options() # 브라우저 꺼짐 방지
#     chrome_optiins.add_experimental_option('detach', True)
#     chrome_optiins.add_experimental_option('excludeSwitches', ['enable-logging']) # 불필요한 에러 메세지 삭제
#     service = Service(executable_path=ChromeDriverManager().install()) # 크롬 드라이버 최신 버전 자동 설치 후 서비스 만들기
        
#     #URL 얻기
#     driver = webdriver.Chrome(service=service,options= chrome_optiins)

#     # 크롬 브라우저 사이즈
#     driver.set_window_size(1400, 1000)
#     # 주소 이동
#     driver.get('https://emes.imi-critical.com/imi_clive/')

#     driver.find_element(By.NAME, 'log_id').send_keys(id)
#     driver.find_element(By.NAME, 'passwd').send_keys(pw)
#     driver.find_element(By.XPATH, '//*[@id="btLogin"]').click()
#     # 5초 까지 대기
#     driver.implicitly_wait(5)

#     # 현재창 인식
#     driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="frMain"]'))

#     # 작업일보 이동
#     driver.find_element(By.XPATH, '//*[@id="div_main_menu"]/ul[1]/li[4]/a').click()
#     driver.find_element(By.XPATH, '//*[@id="div_main_menu"]/ul[1]/li[4]/ul/li[4]/a').click()

#     # 5초 까지 대기
#     driver.implicitly_wait(5)

#     # 작업일보 작성
#     driver.find_element(By.XPATH, '//*[@id="div_top"]/div[1]/button[2]').click()

#     # 5초 까지 대기
#     driver.implicitly_wait(5)

#     # 팀선택
#     driver.find_element(By.XPATH, '//*[@id="div_pop_result"]/div[2]/table/tbody/tr/td[2]/select').click()
#     driver.find_element(By.XPATH, '//*[@id="div_pop_result"]/div[2]/table/tbody/tr/td[2]/select/option[4]').click()

#     # 작업자선택
#     driver.find_element(By.XPATH, f"//select[@name='s_WR_Worker']/option[text()='{name}']").click()

#     for i in range(1,len(timetable)+1):
#         if timetable[i-1]['시작시간'] == '10:00' or timetable[i-1]['시작시간'] == '15:00':
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/select/option[9]').click()
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/input').send_keys('휴식')
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[4]').click()
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/input[1]').send_keys(timetable[i-1]['시작시간'])
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[8]/input[1]').send_keys(timetable[i-1]['종료시간'])
#             continue

#         elif so == '': # and etc == '':
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/select/option[9]').click()
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/input').send_keys(work)
#             # driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[13]/input').send_keys(etc)
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[4]').click()
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/input[1]').send_keys(timetable[i-1]['시작시간'])
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[8]/input[1]').send_keys(timetable[i-1]['종료시간'])
#             continue
        
#         # 샵오더 
#         driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[10]/input').send_keys(so)
#         # # 수량
#         # driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[12]/input').send_keys(수량)

#         # 작업명
#         driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/select/option[11]').click()

#         # 상세내용        
#         driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/input').send_keys(work)
        
#         # 작업코드
#         if finish and i == len(timetable):
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[2]').click()
#         else:
#             driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[3]').click()
            
#         driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/input[1]').send_keys(timetable[i-1]['시작시간'])
#         driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[8]/input[1]').send_keys(timetable[i-1]['종료시간'])
        
#         # OP No
#         driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[11]/select/option[3]').click()

# if name == '김진석' :
#     if prompt := st.chat_input("공지사항"):
#         st.session_state.messages.append({"name": "user", "content": prompt})
        
#     with c1:
#         for message in st.session_state.messages:
#             with st.chat_message(message["name"]):
#                 st.markdown(f"{message['content']}")                
#     # datetime.now().strftime('%Y-%m-%d')
#         if st.session_state.messages:
#             clear = st.button('알림 지우기',use_container_width=True)
#             if clear:
#                 st.session_state.messages.pop()
#                 st.experimental_rerun()

# else:
#     for message in st.session_state.messages:
#         with  st.chat_message(message["name"]):
#             st.markdown(f"{message['content']}")
            
