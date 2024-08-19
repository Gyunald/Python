
import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
from datetime import time
import pyautogui
import pyperclip
import os

st.set_page_config(page_title="GD2😎",layout='wide',initial_sidebar_state='collapsed') # layout='wide','centered', initial_sidebar_state='collapsed','expanded'

current_date = datetime.now().date()
week_number = current_date.isocalendar()[1]

if 'memo' not in st.session_state:
    st.session_state.memo = []

if 'direct' not in st.session_state:
    st.session_state.direct = pd.DataFrame(columns=['샵오더','OP No','상세내용','작업코드','시작시간', '종료시간','수량', '비고'])

if 'messages' not in st.session_state:
    st.session_state.messages = []
 
if 'overtime_data' not in st.session_state:
    st.session_state.overtime_data = pd.DataFrame()


def direct_schedule(start_time, end_time, s2='', s3=''):    
    schedule = st.session_state.direct
    if end_time == '17:00' :
        breaks = [s2, start_time, '10:00', '10:10', '11:45', '12:45', '15:00', '15:20', '17:00', '17:20', s3, end_time]
    else:
        breaks = [s2, start_time, '10:00', '10:10', '11:45', '12:25', '15:00', '15:20', '17:00', '17:20', s3, end_time]
    breaks = sorted(list(set(breaks)))

    if s2 < end_time :
        if start_time == s2  and end_time == s3:
            for i in range(len(breaks) - 1):
                if breaks[i] == '11:45' or breaks[i] == '17:00':
                    continue
                elif start_time < breaks[i + 1] <= end_time:
                    schedule = pd.concat([pd.DataFrame([{'샵오더':'', 'OP No' :'', '상세내용' : indirect, '작업코드': 'ID', '시작시간': breaks[i], '종료시간': breaks[i+1], }]), schedule])
                        
                    if breaks[i] == '10:00' or breaks[i] == "15:00" :
                        schedule = pd.concat([pd.DataFrame([
                            {'상세내용' : '휴식', '작업코드': 'ID','시작시간': breaks[i], '종료시간': breaks[i + 1], }
                            ]), schedule])

        else:
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

                    elif breaks[i] < s3 <= breaks[i+1]:
                        schedule = pd.concat([pd.DataFrame([{'상세내용' : indirect, '작업코드': 'ID', '시작시간': breaks[i], '종료시간': breaks[i+1], }]), schedule])

        schedule=schedule.drop_duplicates(['시작시간','종료시간']).sort_values('시작시간').reset_index(drop=True)
        st.session_state.direct = schedule
        return schedule


    else:
        st.error('시간 확인')

team = (1300, 310)
teams = {'가공' : (1300,390),}

worker = (1600,310)
workers = {'김규덕' : (1600, 360),}


def page(team_click,worker_click):

    pyautogui.click(1900, 800)
    pyautogui.press('home')
    time.sleep(0.2)

    # emes 홈페이지
    pyautogui.click(1200, 20)
    time.sleep(0.1)
    # 작업일보 등록
    pyautogui.click(1550, 220)
    time.sleep(1.5)
    pyautogui.click(team)
    pyautogui.click(team_click)
    time.sleep(.1)
    pyautogui.click(worker)
    time.sleep(.1)
    pyautogui.click(worker_click)
    return

def run_1():
    team_click = teams['가공']
    worker_click = workers['김규덕']

    page(team_click,worker_click)
        
    step = 430
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
            time.sleep(.1)            

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
                time.sleep(.2)
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

            # if st.session_state.direct['상세내용'][i-1] == '세팅' :
            #     pyautogui.press('I')
            #     pyautogui.press('I')
            #     pyautogui.press('I')

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

current_date = datetime.now().date()
st.title(f":orange[{current_date}]")

employee_names = ['김규덕','최종민']
c1, c2, c3, = st.columns(3)
c4, c5, = st.columns([1,.5])

with open('so.txt', "r") as file:
    order = file.readline()

with c1:
    # name = st.selectbox('이름',employee_names,key='name')
    # name = st.radio('이름',employee_names,horizontal=True)
    so = st.text_input('샵오더',value=order)
    op = st.selectbox('OP', ['OP 5','OP 20', 'OP 30', 'OP 40', 'OP 50'], index=1)

    work = st.selectbox('상세내용',['세팅','황삭','정삭','수정','기타'], index=1)
    if work == '기타':
        work = st.text_input('기타',key='work')

    finish = st.checkbox('가공완료')
    if finish :
        수량 = str(st.number_input('수량',1,step=1))

    indirect_check = st.checkbox('간접작업',False)
    
with c2:
    start_time = st.time_input('시작 시간', time(8,0), step=600)
    end_time = st.time_input('종료 시간', time(20,0), step=600)

    etc = st.text_input('비고')
    id ='kdkim'
    pw = 'tnwlr1234!'    
    # links =st.page_link('https://emes.imi-critical.com/imi_clive/',label=':rainbow[EMES_page_link]')

    web = st.link_button('EMES', 'https://emes.imi-critical.com/imi_clive', use_container_width=True)
    add_button = st.button('추가', use_container_width=True)
    botton_run = st.button('등록', use_container_width=True , type= 'primary')

with c3:
    if indirect_check:
        start_time2 = st.time_input('간접작업 시작', time(8, 0), step=600)
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
            
            # for k in st.session_state.direct[st.session_state.direct['시작시간'] < st.session_state.direct['종료시간'].shift(1)].index:
            #     if k in st.session_state.direct.index:
            #         st.session_state.direct.loc[k-1, '종료시간'] = st.session_state.direct.loc[k, '시작시간']
            
            # st.session_state.end = end_time
            st.session_state.start = end_time            
            pyautogui.hotkey('r')
            pyautogui.hotkey('shift','tab')
            pyautogui.hotkey('shift','tab')
            st.rerun()

with c4:
    def adjust_time(time_str):
        time = datetime.strptime(time_str, '%H:%M')
        time = time + timedelta(hours=12)

        return '00:00' if time.strftime('%H:%M') == '23:45' \
            else '01:00' if time.strftime('%H:%M') == '00:25' \
            else '06:00' if time.strftime('%H:%M') == '05:00' \
            else '06:20' if time.strftime('%H:%M') == '05:20' \
            else '07:59' if time.strftime('%H:%M') == '08:00' \
            else time.strftime('%H:%M')

    if week_number % 2 != 0:

        st.session_state.direct['시작시간'] = st.session_state.direct['시작시간'].apply(adjust_time)
        st.session_state.direct['종료시간'] = st.session_state.direct['종료시간'].apply(adjust_time)

    st.session_state.direct = st.session_state.direct.reset_index(drop=True)
    st.dataframe(st.session_state.direct.reset_index(drop=True).fillna(''),use_container_width=True,hide_index=True)

    
    # sl.loc[sl['종료시간'] == '05:00', '종료시간'] = '06:00'
if botton_run:
    with c3:
        try:
            with st.spinner('🎈 업데이트 중'):
                run_1()
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
        os.remove('so.txt')
        with open('so.txt', 'w') as file:
            file.write(so)
    st.session_state.direct = pd.DataFrame(columns=['샵오더','OP No','상세내용','작업코드','시작시간', '종료시간','수량', '비고'])

with c3:
    ed=st.data_editor(pd.DataFrame({
   "메모":[None]

    }),hide_index=True,use_container_width=True,num_rows='dynamic')

    today = str(datetime.today().date().today())

    try:
        overtime = pd.read_excel("G:/PROD/생산공정/Ass`y/이환덕/특근및잔업(식수인원현황)/2024년 식수인원/2024년 식수인원.xlsx",sheet_name=f"{datetime.today().month}월",header=6)

        overtime.columns = overtime.columns.astype(str).str.replace(' 00:00:00','')
        # 부서별
        overtime = overtime[overtime['공정명'] == 'Machining']

    
        index_of_department_column = overtime.columns.get_loc(today)
        overtime['내용'] = overtime.iloc[:,index_of_department_column+1]

        overtime = overtime[['공정명','이름',today,'내용']].fillna('')
        overtime = overtime.rename(columns={today:'근무'})
        overtime['근무'] = overtime['근무'].astype(str)

       
        with st.popover(f":blue[잔업자 명단]",use_container_width=True) :
            st.dataframe(overtime.iloc[:,1:5].sort_values(by='근무',ascending=True),use_container_width=True,hide_index=True,)
    except:
        pass

import streamlit as st
import pandas as pd
from datetime import datetime,timedelta, time as time
import time as t
import pyautogui
import pyperclip
import os

st.set_page_config(page_title="GD2😎",layout='wide',initial_sidebar_state='collapsed') # layout='wide','centered', initial_sidebar_state='collapsed','expanded'

current_date = datetime.now().date()
week_number = current_date.isocalendar()[1]

if 'direct' not in st.session_state:
    st.session_state.direct = pd.DataFrame(columns=['샵오더','OP No','상세내용','작업코드','시작시간', '종료시간','수량', '비고'])

def direct_schedule(start_time, end_time, s2='', s3=''):    
    schedule = st.session_state.direct
    if end_time == '17:00' :
        breaks = [s2, start_time, '10:00', '10:10', '11:45', '12:45', '15:00', '15:20', '17:00', '17:20', s3, end_time]
    else:
        breaks = [s2, start_time, '10:00', '10:10', '11:45', '12:25', '15:00', '15:20', '17:00', '17:20', s3, end_time]
    breaks = sorted(list(set(breaks)))

    if s2 < end_time :
        if start_time == s2  and end_time == s3:
            for i in range(len(breaks) - 1):
                if breaks[i] == '11:45' or breaks[i] == '17:00':
                    continue
                elif start_time < breaks[i + 1] <= end_time:
                    schedule = pd.concat([pd.DataFrame([{'샵오더':'', 'OP No' :'', '상세내용' : indirect, '작업코드': 'ID', '시작시간': breaks[i], '종료시간': breaks[i+1], }]), schedule])
                        
                    if breaks[i] == '10:00' or breaks[i] == "15:00" :
                        schedule = pd.concat([pd.DataFrame([
                            {'상세내용' : '휴식', '작업코드': 'ID','시작시간': breaks[i], '종료시간': breaks[i + 1], }
                            ]), schedule])

        else:
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

                    elif breaks[i] < s3 <= breaks[i+1]:
                        schedule = pd.concat([pd.DataFrame([{'상세내용' : indirect, '작업코드': 'ID', '시작시간': breaks[i], '종료시간': breaks[i+1], }]), schedule])

        schedule=schedule.drop_duplicates(['시작시간','종료시간']).sort_values('시작시간').reset_index(drop=True)
        st.session_state.direct = schedule
        return schedule

    else:
        st.error('시간 확인')

team = (1300, 310)
teams = {'가공' : (1300,380),}

worker = (1600,310)
workers = {'김규덕' : (1600, 350),}

def page(team_click,worker_click):
    pyautogui.click(1900, 800)
    pyautogui.press('home')
    t.sleep(0.5)

    # emes 홈페이지
    pyautogui.click(1300, 20)
    t.sleep(0.1)
    # 작업일보 등록
    pyautogui.click(1530, 220)
    t.sleep(1.5)
    pyautogui.click(team)
    pyautogui.click(team_click)
    t.sleep(.1)
    pyautogui.click(worker)
    t.sleep(.1)
    pyautogui.click(worker_click)
    return

def run_1():
    team_click = teams['가공']
    worker_click = workers['김규덕']

    page(team_click,worker_click)
        
    step = 430
    for i in range(1,len(st.session_state.direct)+1):
        shop_order = 1130, step
        work_name = 1270, step
        details = 1340, step
        start = 1550, step
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
            t.sleep(.1)            

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
                t.sleep(.1)
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
            t.sleep(.2)


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

st.title(f":orange[{current_date}]")

c1, c2, c3, = st.columns(3)
c4, c5, = st.columns([1,.5])

with open('so.txt', "r") as file:
    order = file.readline()

with c1:
    so = st.text_input('샵오더',value=order)
    op = st.selectbox('OP', ['OP 5','OP 10','OP 20', 'OP 30', 'OP 40', 'OP 50'], index=2)

    work = st.selectbox('상세내용',['세팅','황삭','정삭','수정','기타'], index=1)
    if work == '기타':
        work = st.text_input('기타',key='work')

    finish = st.checkbox('가공완료')
    if finish :
        수량 = str(st.number_input('수량',1,step=1))

    indirect_check = st.checkbox('간접작업',False)
    
with c2:
    start_time = st.time_input('시작 시간', time(8,0), step=600)
    end_time = st.time_input('종료 시간', time(20,0), step=600)

    etc = st.text_input('비고')
    id ='kdkim'
    pw = 'tnwlr1234!'

    add_button = st.button('추가', use_container_width=True)
    botton_run = st.button('등록', use_container_width=True , type= 'primary')

    c1,c2 = st.columns(2)
    with c1:
        links =st.page_link('https://emes.imi-critical.com/imi_clive/page/process_plan/work_result_disp.php',label=':blue[Work Result]')
    with c2:
        links =st.page_link('https://emes.imi-critical.com/imi_clive/page/production/shop_order_view.php',label=':orange[Shop Order : View]')

with c3:
    if indirect_check:
        start_time2 = st.time_input('간접작업 시작', time(8, 0), step=600)
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
            
            # for k in st.session_state.direct[st.session_state.direct['시작시간'] < st.session_state.direct['종료시간'].shift(1)].index:
            #     if k in st.session_state.direct.index:
            #         st.session_state.direct.loc[k-1, '종료시간'] = st.session_state.direct.loc[k, '시작시간']
            
            # st.session_state.end = end_time
            st.session_state.start = end_time            
            pyautogui.hotkey('r')
            pyautogui.hotkey('shift','tab')
            pyautogui.hotkey('shift','tab')
            st.rerun()

with c4:
    def adjust_time(time_str):
        time = datetime.strptime(time_str, '%H:%M')
        time = time + timedelta(hours=12)

        return '00:00' if time.strftime('%H:%M') == '23:45' \
            else '01:00' if time.strftime('%H:%M') == '00:25' \
            else '06:00' if time.strftime('%H:%M') == '05:00' \
            else '06:20' if time.strftime('%H:%M') == '05:20' \
            else '07:59' if time.strftime('%H:%M') == '08:00' \
            else time.strftime('%H:%M')

    if week_number % 2 != 0:

        st.session_state.direct['시작시간'] = st.session_state.direct['시작시간'].apply(adjust_time)
        st.session_state.direct['종료시간'] = st.session_state.direct['종료시간'].apply(adjust_time)

st.session_state.direct = st.session_state.direct.reset_index(drop=True)
st.dataframe(st.session_state.direct.reset_index(drop=True).fillna(''),use_container_width=True,hide_index=True)

    
    # sl.loc[sl['종료시간'] == '05:00', '종료시간'] = '06:00'
if botton_run:
    with c3:
        try:
            with st.spinner('🎈 업데이트 중'):
                run_1()
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
        os.remove('so.txt')
        with open('so.txt', 'w') as file:
            file.write(so)

with c3:
    with st.form('memo'):
        with open('note.txt', "r",encoding='UTF8') as file:
            note = file.readlines()
            
        if not note :
            note = sorted({''})
        else:
            note = [i.replace('\n','') for i in note]

        ed=st.data_editor(pd.DataFrame(columns=['인계사항'],data=note), hide_index=True,use_container_width=True,num_rows='dynamic',)

        if st.form_submit_button('저장',use_container_width=True):
            with open('note.txt', 'w', encoding='UTF8') as file2:
                for j in ed.values:
                    file2.write(f"{j[-1]}\n")
            st.rerun()
    
    today = str(datetime.today().date().today())
    
    try:
        overtime = pd.read_excel("G:/PROD/생산공정/Ass`y/이환덕/특근및잔업(식수인원현황)/2024년 식수인원/2024년 식수인원.xlsx",sheet_name=f"{datetime.today().month}월",header=6)

        overtime.columns = overtime.columns.astype(str).str.replace(' 00:00:00','')
        # 부서별
        overtime = overtime[overtime['공정명'] == 'Machining']
    
        index_of_department_column = overtime.columns.get_loc(today)
        overtime['내용'] = overtime.iloc[:,index_of_department_column+1]

        overtime = overtime[['공정명','이름',today,'내용']].fillna('')
        overtime = overtime.rename(columns={today:'근무'})
        overtime['근무'] = overtime['근무'].astype(str)

       
        with st.popover(f":blue[잔업자 명단]",use_container_width=True) :
            st.dataframe(overtime.iloc[:,1:5].sort_values(by='근무',ascending=True),use_container_width=True,hide_index=True,)
    except:
        pass

