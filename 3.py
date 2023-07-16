import streamlit as st
import pandas as pd
from datetime import datetime, time, timedelta

if 'direct' not in st.session_state:
    st.session_state.direct = []

if 'indirect' not in st.session_state:
    st.session_state.indirect = [] 

일정표 = []

출근,퇴근 = time(8,0), time(20,20)
시리얼 = 'A12345'
휴식시간 = [출근, time(10,0),time(10,10),time(11,45),time(12,45),
        time(15,00),time(15,10),time(17,00),time(17,20),퇴근]

for i in range(1,len(휴식시간)):
    if 휴식시간[i-1] == time(10,0) or 휴식시간[i-1] == time(15,0) :
        일정표.append({'시작시간' : 휴식시간[i-1], '종료시간' : 휴식시간[i], '비고' : '휴식'})
        continue
    elif 휴식시간[i-1] == time(11,45) or 휴식시간[i-1] == time(17,0):
        continue
    일정표.append({'시작시간' : 휴식시간[i-1], '종료시간' : 휴식시간[i], '비고' : 시리얼})

일정표2 = 일정표.copy()

일정표2 = pd.DataFrame(일정표2).reset_index(drop=True)
일정표2['시작시간'] = pd.to_datetime(일정표2['시작시간'],format='%H:%M:%S').dt.strftime('%H:%M')
일정표2['종료시간'] = pd.to_datetime(일정표2['종료시간'],format='%H:%M:%S').dt.strftime('%H:%M')
st.dataframe(일정표2)
l = st.session_state.direct
li = st.session_state.indirect
checkbox= st.checkbox('indirect',True)
if checkbox:
    시작 = st.time_input('시작', time(8,00))
    종료 = st.time_input('종료', datetime.combine(datetime.min, 시작) + timedelta(hours=1))
    비고 = st.selectbox('비고', ['회의','교육','청소'])

    추가 = st.button('추가')
    if 추가 :        
        일정표.append({'시작시간' : 시작, '종료시간' : 종료, '비고' : 비고})
        추가일정표 = sorted(일정표, key=lambda x:x['시작시간'])
        
        for j in range(len(추가일정표)) :
            l.append(추가일정표[j]['시작시간'])
            l.append(추가일정표[j]['종료시간'])

        l = sorted(list(set(l)))
        for i in range(1,len(l)):
            if l[i-1] == time(10,0) or l[i-1] == time(15,0) :
                li.append({'시작시간' : l[i-1], '종료시간' : l[i], '비고' : '휴식'})
                continue
            elif l[i-1] == time(11,45) or l[i-1] == time(17,0):
                continue
            elif l[i-1] == 시작 or l[i] == 종료:
                li.append({'시작시간' : l[i-1], '종료시간' : l[i], '비고' : 비고})
                continue
            li.append({'시작시간' : l[i-1], '종료시간' : l[i], '비고' : 시리얼})
            
        li = pd.DataFrame(li).sort_values('종료시간').drop_duplicates(['종료시간']).reset_index(drop=True)
        li = pd.DataFrame(li).sort_values('시작시간').drop_duplicates(['시작시간']).reset_index(drop=True)
        li['시작시간'] = pd.to_datetime(li['시작시간'],format='%H:%M:%S').dt.strftime('%H:%M')
        li['종료시간'] = pd.to_datetime(li['종료시간'],format='%H:%M:%S').dt.strftime('%H:%M')
        
        st.dataframe(li)