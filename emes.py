from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import streamlit as st
import pandas as pd

from datetime import time, datetime, timedelta
st.set_page_config(page_title="IMI e-MES") # layout='wide'


def disable():
    st.session_state.disabled = True

def enable():
    if "disabled" in st.session_state and st.session_state.disabled == True:
        st.session_state.disabled = False

if "disabled" not in st.session_state:
    st.session_state.disabled = False

if 'direct' not in st.session_state:
    st.session_state.direct = pd.DataFrame(columns=['시작시간', '종료시간','상세내용'])

def run():
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

    for i in range(1,len(st.session_state.direct)+1):
        if st.session_state.direct['시작시간'][i-1] == '10:00' or st.session_state.direct['종료시간'][i-1] == '15:00':
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[9]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[6]/input').send_keys(st.session_state.direct['상세내용'][i-1])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/select/option[4]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[9]/input[1]').send_keys(st.session_state.direct['시작시간'][i-1])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[10]/input[1]').send_keys(st.session_state.direct['종료시간'][i-1])
            continue

        elif st.session_state.direct['상세내용'][i-1] != work:
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[9]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[6]/input').send_keys(st.session_state.direct['상세내용'][i-1])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/select/option[4]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[9]/input[1]').send_keys(st.session_state.direct['시작시간'][i-1])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[10]/input[1]').send_keys(st.session_state.direct['종료시간'][i-1])
            continue

        # 샵오더 
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/input').send_keys(so)
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/input').send_keys(Keys.TAB)

        # OP No
        if so != '':
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/select').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[4]/select/option[3]').click()


        # 작업명
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[11]').click()

        # 상세내용        
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[6]/input').send_keys(st.session_state.direct['상세내용'][i-1])
        
        # 작업코드
        if finish and i == len(st.session_state.direct):
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/select/option[2]').click()
        # 수량
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[12]/input').send_keys(수량)
        else:
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/select/option[3]').click()
            

        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[9]/input[1]').send_keys(st.session_state.direct['시작시간'][i-1])
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[10]/input[1]').send_keys(st.session_state.direct['종료시간'][i-1])

        if name == '김진석' and etc != '':
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[13]/input').send_keys(etc)

    # 등록
    driver.find_element(By.XPATH, '//*[@id="div_pop_result"]/div[4]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/div/table/tr[2]/td/button[1]').click()

    st.error('업데이트 완료')
    

def direct_schedule(start_time, end_time, s2='', s3='',):
    schedule = st.session_state.direct
    breaks = [s2, start_time, '10:00', '10:10', '11:45',
            '12:45', '15:00', '15:10', '17:00', '17:20', s3, end_time]
    breaks = sorted(list(set(breaks)))

    if s2 < end_time:
        for i in range(len(breaks) - 1):            
            if start_time <= breaks[i] < end_time:
                if breaks[i] == '10:00' or breaks[i] == "15:00" :
                    schedule = pd.concat([pd.DataFrame([
                        {'시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': '휴식'}
                        ]), schedule])

                elif breaks[i] == '11:45' or breaks[i] == '17:00':
                    continue

                elif work == '' or breaks[i] == s2 or breaks[i+1] == s3:
                    schedule = pd.concat([pd.DataFrame([
                        {'시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': indirect}
                        ]), schedule])

                elif so != '' or start_time < breaks[i+1]:
                    schedule = pd.concat([pd.DataFrame([
                        {'시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': work}
                        ]), schedule])
        schedule=schedule.drop_duplicates(['시작시간']).sort_values('시작시간').reset_index(drop=True)
        st.session_state.direct = schedule
        return schedule
    else:
        st.error('시간 확인')

c1, c2 = st.columns(2)

with c1:
    start_time = st.time_input('시작 시간', time(8, 0), step=600).strftime('%H:%M')
    end_time = st.time_input('종료 시간', time(17, 0), step=600).strftime('%H:%M')
    finish = st.checkbox('가공완료')
    if finish :
        수량 = st.number_input('수량',1,step=1)
    
    e = st.empty()
    indirect_check = e.checkbox('간접작업')

with c2:
    name = st.selectbox('이름', ['김진석','김규덕',])
    e11 = st.empty()
    so = e11.text_input('샵오더')
    if name == '김진석' :
        e11.empty()
        work = st.text_input('상세내용','공정진행')
        etc = st.text_input('비고')
        e.empty()
        indirect_check = e.checkbox('간접작업',value=True)
        
    else:
        work = st.text_input('상세내용')
    id ='kdkim'
    pw = 'xjsld12#'

c4, c5 = st.columns(2)

with c4:
    e1 =st.empty()
    button = e1.button('등록',on_click=disable, disabled=st.session_state.disabled, use_container_width=True,key='b1')

    if indirect_check:        
        e1.empty()
        e = st.empty()
        indirect = e.selectbox('간접작업', ['공정회의','타운홀미팅', '직무교육', '회의', '기타'])
        start_time2 = st.time_input('간접작업 시작', time(8, 0), step=600)
        end_time2 = st.time_input('종료', datetime.combine(datetime.min, start_time2) + timedelta(minutes=30)).strftime('%H:%M')       
        add_button = st.button('추가', use_container_width=True)
        button = st.button('등록', on_click=disable, disabled=st.session_state.disabled,use_container_width=True, key='b2')
        
        if indirect == '기타':
            indirect = e.text_input('기타')
        if add_button:
            with c5:
                new_schedule = direct_schedule(start_time, end_time, start_time2.strftime('%H:%M'), end_time2)
                st.session_state.direct = pd.concat([st.session_state.direct, new_schedule]).drop_duplicates().sort_values(['시작시간','종료시간']).reset_index(drop=True)
                
                for j in st.session_state.direct.loc[st.session_state.direct['시작시간'].duplicated() == True].index:
                    if j in st.session_state.direct.index:
                        st.session_state.direct.drop(index=j, inplace=True)
                
                for k in st.session_state.direct[st.session_state.direct['시작시간'] < st.session_state.direct['종료시간'].shift(1)].index:
                    if k in st.session_state.direct.index:
                        st.session_state.direct.loc[k-1, '종료시간'] = st.session_state.direct.loc[k, '시작시간']
                st.dataframe(st.session_state.direct,use_container_width=True)
        else:
            with c5:
                st.dataframe(st.session_state.direct,use_container_width=True)            
    else:
        st.session_state.direct= pd.DataFrame(columns=['시작시간', '종료시간','상세내용'])
        with c5:
            try:
                schedule = direct_schedule(start_time, end_time)
                st.dataframe(schedule,use_container_width=True)
            except:
                st.info('샵오더,상세내용 입력')

if button :
    if name != '김진석' and so != '' and work != '':
        run()
    elif name == '김진석' and work != '':
        run()

# if name == '김진석' :
#     if prompt := st.chat_input("공지사항"):
#         st.session_state.messages.append({"name": "user", "content": prompt})        

#     for message in st.session_state.messages:
#         with st.chat_message(message["name"]):
#             st.markdown(f"{message['content']} ___ {datetime.now().strftime('%H:%M')}")
#     datetime.now().strftime('%Y-%m-%d')
#     if st.session_state.messages:
#         clear = st.button('알림 지우기',use_container_width=True)
#         if clear:
#             st.session_state.messages.clear()
#             st.experimental_rerun()
# else:
#     for message in st.session_state.messages:
#         with  st.chat_message(message["name"]):
#             st.markdown(f"{message['content']}")