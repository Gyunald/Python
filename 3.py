from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from streamlit_server_state import server_state, server_state_lock
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd
from datetime import time, datetime, timedelta

st.set_page_config(page_title="text") # layout='wide' 

if 'direct' not in st.session_state:
    st.session_state.direct = pd.DataFrame(columns=['샵오더','시작시간', '종료시간','상세내용','비고'])

def run():
    chrome_optiins = Options() # 브라우저 꺼짐 방지
    chrome_optiins.add_experimental_option('detach', True)
    chrome_optiins.add_experimental_option('excludeSwitches', ['enable-logging']) # 불필요한 에러 메세지 삭제
    service = Service(executable_path=ChromeDriverManager().install()) # 크롬 드라이버 최신 버전 자동 설치 후 서비스 만들기
        
    #URL 얻기
    driver = webdriver.Chrome(service=service,options= chrome_optiins)

    # 크롬 브라우저 사이즈
    driver.minimize_window()
    # driver.set_window_size(1400, 1000)
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
        if st.session_state.direct['샵오더'][i-1] == '':
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[5]/select/option[9]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[6]/input').send_keys(st.session_state.direct['상세내용'][i-1])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[7]/select/option[4]').click()
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[9]/input[1]').send_keys(st.session_state.direct['시작시간'][i-1])
            driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[10]/input[1]').send_keys(st.session_state.direct['종료시간'][i-1])
            continue

        # 샵오더 
        driver.find_element(By.XPATH, f'//*[@id="id_{i}"]/td[3]/input').send_keys(st.session_state.direct['샵오더'][i-1])
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

    # # 등록
    # driver.find_element(By.XPATH, '//*[@id="div_pop_result"]/div[4]/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[4]/div/table/tr[2]/td/button[1]').click()
    # driver.close()
    # st.error('업데이트 완료')
    

def direct_schedule(start_time, end_time):
    schedule = st.session_state.direct
    breaks = [start_time, '10:00', '10:10', '11:45',
            '12:45', '15:00', '15:20', '17:00', '17:20', end_time]
    breaks = sorted(list(set(breaks)))

    if start_time < end_time:
        for i in range(len(breaks) - 1):            
            if start_time <= breaks[i] :
                if breaks[i] == '10:00' or breaks[i] == "15:00" :
                    schedule = pd.concat([pd.DataFrame([
                        {'샵오더': '', '시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': '휴식', '비고' : ''}
                        ]), schedule])

                elif breaks[i] == '11:45' or breaks[i] == '17:00':
                    continue
                
                elif indirect !='' and start_time == breaks[i] and end_time == breaks[i+1]:
                    schedule = pd.concat([pd.DataFrame([
                        {'샵오더': '','시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': indirect, '비고' : ''}
                        ]), schedule])

                elif indirect == '' and start_time <= breaks[i+1]:
                    schedule = pd.concat([pd.DataFrame([
                        {'샵오더': so,'시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': work, '비고' : etc}
                        ]), schedule])

                        
        schedule=schedule.drop_duplicates(['시작시간','종료시간']).sort_values('시작시간').reset_index(drop=True)
        st.session_state.direct = schedule
        return schedule
    else:
        st.error('시간 확인')

def on_message_input():
    ot = st.session_state.ot

    if not ot:
        return

    with server_state_lock.ot:
        schedule1 = server_state.ot
        schedule1.loc[schedule1[schedule1['이름'] == name].index, '상세내용'] = work
        schedule1.loc[schedule1[schedule1['이름'] == name].index, '계획'] = st.session_state.r1
        server_state.ot = schedule1
        st.experimental_rerun()

current_week = datetime.today().isocalendar()[1]
date = datetime.now().date()
st.title('테스트 페이지')

name_list = ['김진석','이병호','최재형',
            '김규덕','이호성','김태훈',
            '이영석','임대건','안형철',
            '허남윤','김정훈','황범식',
            '육신현','정대영','박민호']

if current_week % 2 == 0 :
    team = ['이영석', '김정훈', '황범식']
elif current_week % 2 == 1 :
    team = ['임대건', '허남윤', '정대영']

t1,t2 = st.tabs(['작업일보','잔업'])

with t1 :
    add_id = st.radio('선택',['직접','간접'],horizontal=True)
    c1, c2,c3 = st.columns([.5,.5,1])
    with c1:
        indirect = ''
        empty_name = st.empty()
        empty_so = st.empty()
        name = empty_name.selectbox('이름', sorted(name_list))
        so = empty_so.text_input('샵오더')
        empty_work = st.empty()
        start_time = st.time_input('시작 시간', time(8, 0), step=600)
        end_time = st.time_input('종료 시간', time(20, 20), step=600)
        empty_start = st.empty()
        empty_end = st.empty()
        empty_etc = st.empty()
        empty_finish = st.empty()
        
        work = empty_work.text_input('상세내용')

        etc = empty_etc.text_input('비고')
        id ='kdkim'
        pw = 'xjsld12#'
        finish = empty_finish.checkbox('가공완료')
        if finish :
            수량 = st.number_input('수량',1,step=1)
            
        if add_id == '간접': 
            empty_name.empty()
            empty_so.empty()
            empty_work.empty()
            empty_start.empty()
            empty_end.empty()
            empty_etc.empty()
            empty_finish.empty()

            indirect = st.selectbox('상세내용2', ['공정회의','BOM 도면배포','타운홀미팅', '직무교육', '회의', '기타'])
            if indirect == '기타':
                indirect = st.text_input('기타')

        add_button = st.button('추가', use_container_width=True)
        button = st.button('등록', use_container_width=True,key='b1')

        if add_button:
            with c3:
                new_schedule = direct_schedule(start_time.strftime('%H:%M'), end_time.strftime('%H:%M'),)
                st.session_state.direct = pd.concat([st.session_state.direct, new_schedule]).drop_duplicates().sort_values(['시작시간','종료시간']).reset_index(drop=True)
                
                for j in st.session_state.direct.loc[st.session_state.direct['시작시간'].duplicated() == True].index:
                    if j in st.session_state.direct.index:
                        st.session_state.direct.drop(index=j, inplace=True)
                
                for k in st.session_state.direct[st.session_state.direct['시작시간'] < st.session_state.direct['종료시간'].shift(1)].index:
                    if k in st.session_state.direct.index:
                        st.session_state.direct.loc[k-1, '종료시간'] = st.session_state.direct.loc[k, '시작시간']
                st.session_state.direct = st.session_state.direct.reset_index(drop=True)
                st.dataframe(st.session_state.direct.reset_index(drop=True),use_container_width=True,hide_index=True)
                
        else:
            with c3:
                st.dataframe(st.session_state.direct,use_container_width=True,hide_index=True)            


    # if button :
    #     if so != '' and work != '':
    #         run()


with t2:
    c1,c3= st.columns([1.05,1])
    
    with c1:
        with st.form('f1',clear_on_submit=True):
            name = st.selectbox('이름',sorted(name_list),key='n2')
            if not name:
                st.stop()

            with server_state_lock.ot:
                if "ot" not in server_state:
                    server_state.ot = pd.DataFrame(columns=['이름','계획', '상세내용'],
                    index=[i for i in range(1,len(name_list)+1)])
                    server_state.ot['이름'] = [i for i in name_list]
                    server_state.ot['계획'] = ['2교대' if j in team and j in name_list else '1' for j in name_list]

                st.radio('계획',['1','2','3','A','B','C'],index=1,key='r1',horizontal=True,help='''
                1 = 8:00 ~ 17:00\n 
                2 = 8:00 ~ 20:20\n
                3 = 20:20 ~ 23:00\n
                B = 오전 반차\n
                C = 오후 반차\n
                        ''')

            work = st.text_input("상세내용",value=' ', key="ot").strip()
            button = st.form_submit_button('등록',use_container_width=True,type='primary')
            if button :
                on_message_input()

        with c3:
            st.dataframe(server_state.ot.fillna(''),use_container_width=True,hide_index=True,height=563)

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



# for i in range(1,len(st.session_state.direct)+1):
#     i
#     if st.session_state.direct['시작시간'][i-1] == '10:00' or st.session_state.direct['종료시간'][i-1] == '15:00':
#         st.session_state.direct['샵오더'][i-1]
#         st.session_state.direct['시작시간'][i-1]
#         st.session_state.direct['종료시간'][i-1]
#         st.session_state.direct['상세내용'][i-1]
#         continue

#     elif st.session_state.direct['샵오더'][i-1] == '':
#         st.session_state.direct['샵오더'][i-1]
#         st.session_state.direct['시작시간'][i-1]
#         st.session_state.direct['종료시간'][i-1]
#         st.session_state.direct['상세내용'][i-1]
#         continue

#     # 샵오더 
#     so

#     # 상세내용        
#     st.session_state.direct['상세내용'][i-1]
    
#     st.session_state.direct['시작시간'][i-1]
#     st.session_state.direct['종료시간'][i-1]
