import streamlit as st
import pandas as pd
from datetime import datetime,timedelta, time as dt_time
import time as t
import pyautogui
import pyperclip

st.set_page_config(page_title="GD2😎",layout='wide',initial_sidebar_state='collapsed') # layout='wide','centered', initial_sidebar_state='collapsed','expanded'

if 'direct' not in st.session_state:
    st.session_state.direct = pd.DataFrame(columns=['샵오더','OP No','상세내용','작업코드','시작시간', '종료시간','수량', '비고'])

if 'messages' not in st.session_state:
    st.session_state.messages = []
 
if 'overtime_data' not in st.session_state:
    st.session_state.overtime_data = pd.DataFrame()

def direct_schedule(start_time, end_time, s2='', s3=''):
    schedule = st.session_state.direct
    breaks = [s2, start_time, '10:00', '10:10', '11:45', '12:45', '15:00', '15:10', '17:00', '17:20', s3, end_time]
    breaks = sorted(list(set(breaks)))

    if s2 < end_time:
        for i in range(len(breaks) - 1):
            if breaks[i] == '11:45' or breaks[i] == '17:00':
                continue
            elif start_time < breaks[i + 1] <= end_time:
                schedule = pd.concat([pd.DataFrame([{'샵오더' : so, 'OP No' : op,  '상세내용' : work,'작업코드': 'I', '시작시간': breaks[i], '종료시간': breaks[i + 1], '수량':'', '비고' : etc}]), schedule])
                
                if breaks[i+1] == end_time and finish == True:
                    schedule = pd.concat([pd.DataFrame([{'샵오더' : so, 'OP No' : op,  '상세내용' : work,'작업코드': 'F', '시작시간': breaks[i], '종료시간': breaks[i + 1], '수량': 수량, '비고' : etc}]), schedule])
                    
                if breaks[i] == '10:00' or breaks[i] == "15:00" :
                    schedule = pd.concat([pd.DataFrame([
                        {'상세내용' : '휴식', '작업코드': 'ID','시작시간': breaks[i], '종료시간': breaks[i + 1], }
                        ]), schedule])

                elif breaks[i] <= s3 <= breaks[i+1]:
                    schedule = pd.concat([pd.DataFrame([{'상세내용' : indirect, '작업코드': 'ID', '시작시간': breaks[i], '종료시간': breaks[i+1], }]), schedule])

        schedule=schedule.drop_duplicates(['시작시간','종료시간']).sort_values('시작시간').reset_index(drop=True)
        st.session_state.direct = schedule
        return schedule
    else:
        st.error('시간 확인')

def run():
    pyautogui.click(1900, 800)
    pyautogui.press('home')
    t.sleep(0.2)
    team = 1300, 300 
    team_click = team[0], team[1]+70
    worker = team[0]+300, 300
    worker_click = worker[0], worker[1]+30

    # emes 홈페이지
    pyautogui.click(1200, 20)
    t.sleep(0.1)
    # 작업일보 등록
    pyautogui.click(1550, 180)
    t.sleep(1.5)
    pyautogui.click(team)
    pyautogui.click(team_click)
    t.sleep(.1) 
    pyautogui.click(worker)
    t.sleep(.1)
    pyautogui.click(worker_click)
        
    step = 410
    for i in range(1,len(st.session_state.direct)+1):
        shop_order = 1150, step
        work_name = 1270, step
        details = 1340, step
        start = 1580, step
        end = 1630, step
        count = 1730, step
        submit = 1350, 920

        if st.session_state.direct['작업코드'][i-1] == 'ID':
            # 작업명
            pyautogui.click(work_name)
            pyautogui.press('I')
            pyautogui.press('tab')
            pyautogui.press('tab')
            
            # 상세내용
            pyautogui.click(details)
            pyperclip.copy(st.session_state.direct['상세내용'][i-1])
            pyautogui.hotkey('ctrl','v')

            # 시간
            pyautogui.click(start)
            pyautogui.typewrite(st.session_state.direct['시작시간'][i-1])
            pyautogui.click(end)
            pyautogui.typewrite(st.session_state.direct['종료시간'][i-1])
            step += 33

            continue
    
        else:
            if st.session_state.direct['샵오더'][i-1] != '':
                # 샵오더
                pyautogui.click(shop_order)
                pyperclip.copy(st.session_state.direct['샵오더'][i-1])
                pyautogui.hotkey('ctrl','v')
                t.sleep(.2)
                pyautogui.press('tab')
                
                # OP NO
                down = st.session_state.direct['OP No'][i-1].split(' ')[1][0]

                for tab in range(int(down)):
                    pyautogui.press('down')
                pyautogui.press('tab')

            # 작업명
            pyautogui.click(work_name)
            pyautogui.press('M')
            pyautogui.press('tab')
            pyautogui.press('tab')

            # 상세내용
            pyperclip.copy(st.session_state.direct['상세내용'][i-1])
            pyautogui.hotkey('ctrl','v')
            pyautogui.press('tab')

            # 작업코드
            if st.session_state.direct['작업코드'][i-1] == 'F':
                pyautogui.press('F')
                # 수량
                pyautogui.click(count)
                pyautogui.typewrite(st.session_state.direct['수량'][i-1])

            else:
                pyautogui.press('I')

            # 시작시간
            pyautogui.click(start)
            pyautogui.typewrite(st.session_state.direct['시작시간'][i-1])
            # 종료시간
            pyautogui.press('tab')
            pyautogui.typewrite(st.session_state.direct['종료시간'][i-1])
            pyautogui.press('tab')

            # 비고
            if st.session_state.direct['비고'][i-1] != '' :                    
                pyperclip.copy(st.session_state.direct['비고'][i-1])
                pyautogui.hotkey('ctrl','v')                    
            step += 33

    # pyautogui.click(submit)
    # pyautogui.press('enter')
    return

# img = st.image('1.gif')

current_date = datetime.now().date()
st.title(current_date)

employee_names = ['김규덕']
c1, c2, c3, = st.columns(3)

with c1:
    name = st.selectbox('이름',employee_names,key='name')
    so = st.text_input('샵오더')
    op = st.selectbox('OP', ['OP 10','OP 20', 'OP 30', 'OP 40', 'OP 50', 'OP 60'], index=1)

    work = st.selectbox('상세내용',['세팅','황삭','정삭','수정','기타'], index=1)
    if work == '기타':
        work = st.text_input('기타',key='work')

    finish = st.checkbox('가공완료')
    if finish :
        수량 = str(st.number_input('수량',1,step=1))

    indirect_check = st.checkbox('간접작업',False)

with c2:
    start_time = st.time_input('시작 시간', dt_time(8,0), step=600)
    end_time = st.time_input('종료 시간', dt_time(20,20), step=600)
    
    etc = st.text_input('비고')
    id ='kdkim'
    pw = 'xjsld12#'    
    add_button = st.button('추가', use_container_width=True)
    botton_run = st.button('등록', use_container_width=True , type= 'primary')
    web = st.link_button('EMES', 'https://emes.imi-critical.com/imi_clive', use_container_width=True)

with c3:
    if indirect_check:
        start_time2 = st.time_input('간접작업 시작', dt_time(8, 0), step=600)
        end_time2 = st.time_input('간접작업 종료',(datetime.combine(datetime.min, start_time2) + timedelta(minutes=30)).time(),step=600)
        indirect = st.selectbox('간접작업', ['생산회의', '작업계획수립 및 BOM 출력','타운홀미팅', '직무교육','회의', '청소', '기타'])

        if indirect == '기타':
            indirect = st.text_input('기타', key='indirect')
    
        if add_button:
            new_schedule = direct_schedule(start_time.strftime('%H:%M'), end_time.strftime('%H:%M'), start_time2.strftime('%H:%M'), end_time2.strftime('%H:%M'))
            st.session_state.direct = pd.concat([st.session_state.direct, new_schedule]).drop_duplicates().sort_values(['시작시간','종료시간']).reset_index(drop=True)
            
            for j in st.session_state.direct.loc[st.session_state.direct['시작시간'].duplicated() == True].index:
                if j in st.session_state.direct.index:
                    st.session_state.direct.drop(index=j, inplace=True)
            
            for k in st.session_state.direct[st.session_state.direct['시작시간'] < st.session_state.direct['종료시간'].shift(1)].index:
                if k in st.session_state.direct.index:
                    st.session_state.direct.loc[k-1, '종료시간'] = st.session_state.direct.loc[k, '시작시간']

    else:
        if add_button:
            new_schedule = direct_schedule(start_time.strftime('%H:%M'), end_time.strftime('%H:%M'))
            st.session_state.direct = pd.concat([st.session_state.direct, new_schedule]).drop_duplicates().sort_values(['시작시간','종료시간']).reset_index(drop=True)
            
            for j in st.session_state.direct.loc[st.session_state.direct['시작시간'].duplicated() == True].index:
                if j in st.session_state.direct.index:
                    st.session_state.direct.drop(index=j, inplace=True)
            
            for k in st.session_state.direct[st.session_state.direct['시작시간'] < st.session_state.direct['종료시간'].shift(1)].index:
                if k in st.session_state.direct.index:
                    st.session_state.direct.loc[k-1, '종료시간'] = st.session_state.direct.loc[k, '시작시간']
            st.toast('등록은 한 번만 누르세요', icon ='🙏')
    pyautogui.press('home')
    t.sleep(.5)

st.session_state.direct = st.session_state.direct.reset_index(drop=True)
st.dataframe(st.session_state.direct.reset_index(drop=True).fillna(''),use_container_width=True,hide_index=True)

if botton_run:
    with c3:
        try:
            with st.spinner('🎈 업데이트 중'):
                run()
            st.write('###')
            st.info('등록 완료 🙉')
            st.toast('수정 or 삭제는 홈페이지에서', icon ='💡')

        except Exception as e:
            with c3:
                st.write('###')
                a = [st.session_state.direct['샵오더'][i] for i in st.session_state.direct[st.session_state.direct['작업코드'] == 'F'].index]
                st.error(f"""
                등록 실패 🙈\n
                잔여수량 가공완료 확인\n
                {' , '.join(a)}
                """)
                # st.write(e)
    st.session_state.direct = pd.DataFrame(columns=['샵오더','OP No','상세내용','작업코드','시작시간', '종료시간','수량', '비고'])
