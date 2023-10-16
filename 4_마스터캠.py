import streamlit as st
import pygetwindow as gw
import pyautogui as pi
import time
import math
import matplotlib.pyplot as plt
import os
import subprocess

if 'lines' not in st.session_state:
    st.session_state.lines = []
if 'arcs' not in st.session_state:
    st.session_state.arcs = []


t1, t2, t3 = st.tabs(['파일열기', '도면그리기', '빗변길이'])
with t1:

    def search_subfolders(directory):
        subfolders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
        selected_part = st.selectbox('파트 선택', subfolders,index=None)
    
        if selected_part:
            part_path = os.path.join(directory, selected_part)
            part_files = os.listdir(part_path)
            selected_serial = st.selectbox('시리얼 선택', part_files, index=None)

            if selected_serial:
                serial_path = os.path.join(part_path, selected_serial)
                serial_files = os.listdir(serial_path)

                mastercam_executable = "C:/Program Files/mcamX9/Mastercam.exe"
                for file in serial_files:
                    file_name = os.path.splitext(file)[0]
                    if st.button(file_name):
                        file_path = os.path.join(serial_path, file)
                        subprocess.run([mastercam_executable, file_path])
    def main():
        directory = 'C:/Users/kdkim/Desktop/Modeling'
        search_subfolders(directory)

    if __name__ == "__main__":
        main()

with t2 :
    c1 = st.columns(4)
    with c1[0]:
        with st.form('line',clear_on_submit=True) :

            lines = st.text_input('lines',placeholder='x,z x,c')
            bt_lines = st.form_submit_button('lines')
            pop = st.form_submit_button('pop')
            if pop :
                st.session_state.lines.pop()
                st.rerun()
                
            if bt_lines:
                st.session_state.lines.append(list(coord if coord else None for coord in lines.split(',')))
                previous_value = None

                for c, (i, j) in enumerate(st.session_state.lines):                
                    if i is None:
                        i = float(previous_value[0])
                        st.session_state.lines[c][0] = i
                    if j is None:
                        j = float(previous_value[1])
                        st.session_state.lines[c][1] = j

                    if 'c' in str(i) :
                        각도 = float(str(st.session_state.lines[c][0]).replace('c',''))
                        side_a = (float(st.session_state.lines[c][1]) - float(st.session_state.lines[c-1][1])) * 2  # 한 변의 길이
                        angle_radians = math.radians(float(각도))
                        side_b = side_a * math.tan(angle_radians)
                        st.session_state.lines[c][0] = float(str(abs(round(float(st.session_state.lines[c-1][0]) + abs(side_b),3))))

                    if 'c' in str(j) :
                        길이 = (float(st.session_state.lines[c][0]) - float(st.session_state.lines[c-1][0])) / 2
                        각도 = float(str(st.session_state.lines[c][1]).replace('c',''))
                        side_a = float(길이) # 한 변의 길이
                        angle_radians = math.radians(float(각도))
                        side_b = side_a * math.tan(angle_radians)

                        if st.session_state.lines[0][1] == '0':
                            st.session_state.lines[c][1] = float(str(abs(round(float(st.session_state.lines[c-1][1]) + abs(side_b),3))))

                        elif st.session_state.lines[0][1] != '0':
                            st.session_state.lines[c][1] = float(str(abs(round(float(st.session_state.lines[c-1][1]) - abs(side_b),3))))

                    if '-' in str(i) :
                        st.session_state.lines[c][0] = float(st.session_state.lines[c][0].replace('-',''))
                        
                        st.session_state.lines[c][0] = (float(st.session_state.lines[c-1][0]) - float(st.session_state.lines[c][0])) * 2

                    if '+' in str(i) :
                        st.session_state.lines[c][0] = float(st.session_state.lines[c][0].replace('+',''))
                        
                        st.session_state.lines[c][0] = float(st.session_state.lines[c-1][0]) + st.session_state.lines[c][0] * 2

                    if '-' in str(j):
                        st.session_state.lines[c][1] = float(str(st.session_state.lines[c][1]).replace('-',''))
                        
                        st.session_state.lines[c][1] = float(st.session_state.lines[c-1][1]) - float(st.session_state.lines[c][1])

                    if '+' in str(j):
                        st.session_state.lines[c][1] = str(st.session_state.lines[c][1]).replace('+','')
                        
                        st.session_state.lines[c][1] = float(st.session_state.lines[c-1][1]) + float(st.session_state.lines[c][1])
                        
                    current_value = st.session_state.lines[c][0], st.session_state.lines[c][1]
                    previous_value = current_value
            run_s = st.form_submit_button('실행')

    with c1[2]:
        st.write(':rainbow[lines]')
        for i,j in st.session_state.lines:
            round(float(i),3),round(float(j),3)

    with c1[1]:        
        with st.form('arc',clear_on_submit=True) :
            arcs = st.text_input('arcs', placeholder='z,r')
            bt_arcs = st.form_submit_button('arcs')
            pop2 = st.form_submit_button('pop2')
            if pop2 :
                st.session_state.arcs.pop()
                st.rerun()

            if bt_arcs:
                st.session_state.arcs.append(list(coord if coord else None for coord in arcs.split(',')))
                previous_value = None

                for c, (z, r) in enumerate(st.session_state.arcs):
                    if z is None:
                        z = previous_value[1] if previous_value else 0
                        st.session_state.arcs[c][1] = z

                    if 'r' in str(r) :
                        st.session_state.arcs[c][2] = st.session_state.arcs[c][2].replace('r','')

                    current_value = z, r
                    previous_value = current_value
            run_s2 = st.form_submit_button('실행2')
                
    with c1[3]:
        st.write(':rainbow[arcs]')    
        for z,r in st.session_state.arcs:
            round(float(z),3),round(float(r),3)

    if run_s:
        app_name = "mastercam" 

        edge_windows = gw.getWindowsWithTitle(app_name)[0]
        try:
            if edge_windows.isActive == False:
                edge_windows.activate()
            edge_windows.restore()
            if edge_windows.isMaximized == False:
                edge_windows.maximize()
        except Exception as e:
            edge_windows.minimize()
            edge_windows.maximize()

        time.sleep(.2)
    
        pi.press('alt')
        pi.press('c')
        pi.press('l')
        pi.press('e')
        time.sleep(1)
        pi.click(189, 143)

        for x,z in st.session_state.lines:
            pi.typewrite(f"{x},-{abs(float(z))}")
            pi.press('enter') 
            time.sleep(.1)

        pi.click(189, 143)
        pi.press('esc')
        pi.press('esc')

        # arcs
        if  st.session_state.arcs:
            pi.press('alt')
            pi.press('c')
            pi.press('a')
            pi.press('c')
            time.sleep(1)

            for z,r in st.session_state.arcs:
                pi.typewrite(f"0,-{abs(float(z))}")
                pi.press('enter') 
                pi.press('r') 
                pi.typewrite(r)
                pi.press('enter')
                time.sleep(.1)
            pi.press('esc')
            pi.press('esc')

    x_values = []
    z_values = []

    for k,q in st.session_state.lines:
        current_value_x = float(k)
        current_value_z = float(q)
        x_values.append(current_value_x)
        z_values.append(current_value_z)
    try:
        first_index = x_values.index(x_values[0])  # 첫 번째 'c'의 인덱스를 찾습니다.
        second_c_index = x_values.index(x_values[0], first_index + 1)  # 첫 번째 'c' 이후부터 다시 'c'를 찾습니다.

        # 그래프 생성
        a = plt.figure(figsize=(8, 6))  # 그래프 크기 설정
        color = 'r'

        plt.plot(x_values, z_values, linestyle='-', color=color)  # x, z 데이터로 그래프 생성
        # plt.plot(x_values[second_c_index:], z_values[second_c_index:], linestyle='-', color=color)  # x, z 데이터로 그래프 생성

        plt.title('X-Z')  # 그래프 제목 설정
        plt.xlabel('X')  # x축 레이블 설정
        plt.ylabel('Z')  # z축 레이블 설정
        plt.xlim(0,max(x_values)*2)  # x축 범위 설정
        plt.ylim(max(z_values)*4,-1)  # z축 범위 설정

        # 그래프 표시
        plt.grid(True)  # 격자 표시
        st.pyplot(a)
    except:
        pass

with t3:
    c1,c2 = st.columns([.5,2])

    with c1:
        # 각도와 한 변의 길이
        a = st.number_input('한 변의 길이',value=None)
        c = st.number_input('각도',value=None)

        if a and c :
            with c2:
                # 각도를 라디안으로 변환합니다.
                c_rad = math.radians(c)

                # 빗변(b)의 길이를 삼각함수를 사용하여 계산합니다.
                b = a / math.cos(c_rad)

                # 높이(h)를 삼각함수를 사용하여 계산합니다.
                h = a * math.tan(c_rad)

                g = plt.figure(figsize=(6, 3))  # 그래프 크기 설정

                # 꼭지점 좌표
                x = [0, a, 0]
                y = [0, 0, h]

                plt.plot(x + [x[0]], y + [y[0]], 'o-')
                plt.annotate(f'a = {a:.3f}', ((a / 3) , .1))
                plt.annotate(f'b = {b:.3f}', (a / 2, (h / 2)+.1))
                plt.annotate(f'c = {c}°', (a /1.5, .1))
                plt.annotate(f'h = {h:.3f}', (.1, h / 2))
                plt.xlabel('x')
                plt.ylabel('y')
                plt.axis('equal')
                # plt.grid(True)
                st.pyplot(g)
