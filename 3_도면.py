import streamlit as st
import webbrowser
import time as t
import pyautogui
import pdfplumber
import re
from PIL import Image
import pandas as pd

l = 'C:/Users/kdkim/Desktop/python/EMES/pdf_drawing.txt'
with open(l,'r') as f:
    f = f.readlines()
c1,c2,c3 = st.columns([1,.5,1])

list_selecbox = [i.split('\\')[-1].replace('.pdf\n','') for i in f]

with c1:
    serial = st.selectbox('시리얼넘버',set(list_selecbox), index=None)

    if serial :
        matching_lines = [line.strip() for line in f if serial[:-1] in line]

        st.write('###')
        for i in matching_lines:
            try:
                if st.button(i.split('\\')[-1].replace('.pdf',''),use_container_width=True):
                    # st.write(f"file:///{i}")
                    webbrowser.open(i)
                    t.sleep(1.5)
                    pyautogui.hotkey('ctrl',']')
            except:
                pass

        for i in matching_lines:
            if serial.strip() in i :
                serial = i

with c2:
    page = st.text_input('페이지')
with c3:
    c4,c5= st.columns([1,1])
    with c4:
        st.write('###')
        conversion1 = st.toggle('평면도')

    with c5:
        st.write('###')
        conversion2 = st.toggle('테이블')

        if conversion2 :
            row = st.text_input('몇번째 행')

if page and conversion1:
    dpyautogui=120
    thread_count=1
    first_page = page
    last_page = page
    st.write('---')

    def is_valid_float(text):
        text = text[::-1]
        if '.' in text and any(char.isdigit() for char in text) and all(char in '-0123456789RC./ ' for char in text):
            return True
        return False
    
    with st.spinner('단위 변환 중'):
        with pdfplumber.open(serial) as pdf:
            p0 = pdf.pages[int(page)-1]
            tables = p0.dedupe_chars(tolerance=1).extract_words(x_tolerance=1, y_tolerance=1,horizontal_ltr=False, vertical_ttb=False,)
            im = p0.to_image(resolution=200,antialias=True)
            im.draw_rects(p0.extract_words(x_tolerance=1, y_tolerance=1,horizontal_ltr=False, vertical_ttb=False,))
            # im.show()
            serial = serial.split('\\')[-1].replace('.pdf','')
            im.save(f"C:/Users/kdkim/Desktop/python/EMES/{serial}.png", format="PNG", quantize=False,)

        drawing = {}
        images = Image.open(f"C:/Users/kdkim/Desktop/python/EMES/{serial}.png")

        width, height = images.size
        if width < height :
            image = images.rotate(-90, expand=True)
        else:
            image = images.rotate(0, expand=True)
        with st.expander('탐지된 요소'):
            st.image(image)
            for item in tables:
                text = item['text']

                if is_valid_float(text):
                    try:
                        if '-' in text :
                            n = text.split('-')
                            for i in n :
                                drawing[f"TAP {i}"] = f"{float(i)*25.4 :.2f}"
                        elif '/' in text :
                            n = text.split('/')
                            for i in n :
                                drawing[i] = f"{float(i)*25.4 :.2f}"
                        elif 'R' in text :
                            drawing[text] = f"{float(text.replace('R',''))*25.4 :.2f}"
                        
                        else:
                            drawing[text] = f"{float(text)*25.4 :.2f}"
                    except:
                        pass
        df =pd.DataFrame({'inch' : drawing.keys(), 'mm' : drawing.values()},)
        df = df.sort_values('inch',ascending=True).reset_index(drop=True)
        c = 0
        for i in range((len(df)//15) + 1):
            c += 15
            st.dataframe(df[c-15:c].T,use_container_width=True)


elif page and conversion2 :
    if row != '':
        with st.spinner('단위 변환 중') :
            with pdfplumber.open(serial) as pdf:
                p0 = pdf.pages[int(page)-1]
                tables = p0.dedupe_chars(tolerance=1).extract_words(x_tolerance=1, y_tolerance=1,horizontal_ltr=False, vertical_ttb=False,)
                im = p0.to_image(resolution=200,antialias=True)
                im.draw_rects(p0.extract_words(x_tolerance=1, y_tolerance=1,horizontal_ltr=False, vertical_ttb=False,))
                # im.show()
                serial = serial.split('\\')[-1].replace('.pdf','')
                im.save(f"C:/Users/kdkim/Desktop/python/EMES/{serial}.png", format="PNG", quantize=False,)

            table = {}
            images = Image.open(f"C:/Users/kdkim/Desktop/python/EMES/{serial}.png")

            width, height = images.size
            if width < height :
                image = images.rotate(-90, expand=True)
            else:
                image = images.rotate(0, expand=True)
            with st.expander('탐지된 요소'):
                st.image(image)
            # pdf = pdfplumber.open(tables)

            page = int(page)
            # row = st.text_input('행', value=1, help='위에서부터 1행')
            p0 = pdf.pages[page-1]
            tables = p0.extract_tables()

            loop_list = range(-1,-10,-1)

            for loop in loop_list:
                try: 
                    for i in tables[loop][::-1]:
                        try:
                            i[int(row)]=i[int(row)].replace('. ','')
                            # if i[row].strip():
                            i = re.sub(r'[^0-9.]', ' ', i[int(row)][::-1]).split(' ')
                            for q in i :
                                try:
                                    if q.isdigit() == False :
                                        q = float(q)
                                        table[q] = f"{float(q*25.4) :.2f}"
                                except :
                                    pass
                        except :
                            continue
                except :
                    continue
            df = pd.DataFrame({'inch' : table.keys(), 'mm' : table.values()})
            df = df.sort_values('inch',ascending=True).reset_index(drop=True)
            c = 0
            for i in range((len(df)//15) + 1):
                c += 15
                st.dataframe(df[c-15:c].T,use_container_width=True)