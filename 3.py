from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import streamlit as st
import pandas as pd
from datetime import time, datetime, timedelta

if 'direct' not in st.session_state:
    st.session_state.direct = pd.DataFrame(columns=['샵오더', '시작시간', '종료시간','상세내용','비고'])

def direct_schedule(start_time, end_time, s2='', s3=''):
    schedule = st.session_state.direct
    breaks = [s2, start_time, '10:00', '10:10', '11:45', '12:45', '15:00', '15:10', '17:00', '17:20', s3, end_time]
    breaks = sorted(list(set(breaks)))

    if s2 < end_time:
        for i in range(len(breaks) - 1):
            if breaks[i] == '10:00' or breaks[i] == "15:00" :
                schedule = pd.concat([pd.DataFrame([
                    {'샵오더': '', '시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용': '휴식', '비고' : ''}
                    ]), schedule])
            elif breaks[i] == '11:45' or breaks[i] == '17:00':
                continue

            elif start_time < breaks[i + 1] <= end_time:
                schedule = pd.concat([pd.DataFrame([{'샵오더' : so, '시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용' : work, '비고' : etc}]), schedule])

                if s2 != '' and s2 < breaks[i + 1] <= s3:
                    schedule = pd.concat([pd.DataFrame([{'샵오더' : '', '시작시간': breaks[i], '종료시간': breaks[i + 1], '상세내용' : indirect, '비고' : ''}]), schedule])

        schedule=schedule.drop_duplicates(['시작시간','종료시간']).sort_values('시작시간').reset_index(drop=True)
        st.session_state.direct = schedule
        return schedule
    else:
        st.error('시간 확인')

# Streamlit UI
c1, c2 = st.columns(2)

with c1:

    start_time = st.time_input('시작 시간', time(8,0), step=600)
    end_time = st.time_input('종료 시간', time(17,0), step=600)

    finish = st.checkbox('가공완료')
    indirect_check = st.checkbox('간접작업')
with c2:
    name = '김규덕'
    so = st.text_input('샵오더')
    work = st.text_input('상세내용')
    etc = st.text_input('비고')
    id ='kdkim'
    pw = 'xjsld12#'    

c4, c5 = st.columns(2)

with c4:
    if indirect_check:
        e = st.empty()
        indirect = e.selectbox('간접작업', ['타운홀미팅', '직무교육','회의', '기타'])
        start_time2 = st.time_input('간접작업 시작', time(8, 0), step=600)
        end_time2 = st.time_input('간접작업 종료',
                                (datetime.combine(datetime.min, start_time2) + timedelta(minutes=30)).time(),
                                step=600)
        
        if indirect == '기타':
            indirect = e.text_input('기타')
    add_button = st.button('추가', use_container_width=True)
    run_indirect = st.button('등록', use_container_width=True)
    
    if add_button:
        with c5:
            if len(st.session_state.direct) > 1 :                
                new_schedule = direct_schedule(start_time.strftime('%H:%M'), end_time.strftime('%H:%M'), start_time2.strftime('%H:%M'), end_time2.strftime('%H:%M'))
                st.session_state.direct = pd.concat([st.session_state.direct, new_schedule]).drop_duplicates().sort_values(['시작시간','종료시간']).reset_index(drop=True)

            else:
                new_schedule = direct_schedule(start_time.strftime('%H:%M'), end_time.strftime('%H:%M'))
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
        with c5:
            st.dataframe(st.session_state.direct, hide_index=True, use_container_width=True)

