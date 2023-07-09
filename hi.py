import streamlit as st
import datetime
import pandas as pd
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

        # elif schedule[-1]['종료시간'] > end_time:
        #     schedule[-1]['종료시간'] = end_time

        return schedule
    except:
        return None

# 시작 시간과 종료 시간 입력
start_time = st.time_input('시작 시간', value=datetime.time(8, 0)).strftime('%H:%M')
end_time = st.time_input('종료 시간', value=datetime.time(20, 20)).strftime('%H:%M')

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

        st.dataframe(df)
    else:
        st.error('시간 확인')
