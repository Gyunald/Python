import streamlit as st
import pandas as pd
import datetime

def generate_work_schedule(start_time, end_time):
    # 근무시간과 쉬는시간 설정    
    start = start_time,'10:00', '10:10', '12:00', '13:00', '15:00', '15:10', '17:00', '17:20', end_time

    # 데이터프레임 생성
    schedule = pd.DataFrame(columns=['시작시간', '종료시간'])

    # 근무시간 및 쉬는시간 추가
    for c in range(len(start)):
        if start[c] < end_time :
            if start[c] == '12:00':
                continue
            elif start[c] == '17:00':
                continue
            schedule = pd.concat([schedule, pd.DataFrame({'시작시간': [start[c]],
                                                        '종료시간': [start[c+1]]})])
        elif len(schedule) == 1 :
            schedule.iloc[0] = [start_time,end_time]

        elif schedule['종료시간'].iloc[-1] > end_time:
            schedule.iloc[-1] = [start[c-1], end_time]
    
    return schedule.reset_index(drop=True)
# 시작 시간과 종료 시간 입력
start_time = st.time_input('시작 시간', value=datetime.time(8, 0)).strftime('%H:%M')
end_time = st.time_input('종료 시간', value=datetime.time(17, 0)).strftime('%H:%M')

# 근무시간표 생성
schedule = generate_work_schedule(start_time, end_time)

# 결과 출력
st.write(schedule)
