import streamlit as st
import pandas as pd
import qrcode

def generate_qrcode(number):
        qr = qrcode.make(number).resize((150, 150))
        return qr

def convert_to_special_char(char):
    key_mappyautoguing = {
        '0': ')',
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '&',
        '8': '*',
        '9': '(',
        '`': '~',
        '-': '_',
        '=': '+'
    }
    return key_mappyautoguing.get(char, char)

def convert_string_to_special(input_string):
    return ''.join(convert_to_special_char(char) for char in input_string)

path1 = "C:/Users/kdkim/Desktop/PO23.csv"
path2 = "C:/Users/kdkim/Desktop/OSM23.csv"
a1 = pd.read_csv(path1, header=9,)
a2 = pd.read_csv(path2, header=10,)

df = pd.merge(a1[['Part Name','Material','Heat No.']], a2[['Serial no.','Part Name','Part Number']], on='Part Name', how='outer').drop_duplicates().fillna('')
df.columns = df.columns.str.replace('.','').str.strip()

pn = st.selectbox('시리얼넘버',sorted([i for i in df['Serial no'].drop_duplicates()]),placeholder='검색 또는 선택', index=None)
if pn:
    df = df[df['Serial no'].str.contains(pn,case=False)].reset_index(drop=True)
    df['QRcode'] = False

if pn :
    word = ['ASTM/ASME','ASTM','ASME', 'A/S','SA/','/','Type1',]
    for i in word:
        df['Material'] = df['Material'].str.replace(i,'').str.strip()
    for j in ',;:':
        df['Part Name'] = df['Part Name'].str.strip().str.split(j).str[0].str.upper()
    df = df[['Part Name','Serial no','Material','Heat No', 'Part Number',"QRcode"]]
    df.rename(columns={'Serial no' : 'Serial No'}, inplace=True)

    t3_c = st.empty()                
    
    q = st.data_editor(
        df.reindex(columns=['QRcode','Part Name', 'Serial No', 'Material', 'Heat No', 'Part Number']),
        key='q',
        use_container_width=True,
        hide_index=True,            
        )

    index = q.loc[q['QRcode'] == True].index

    if len(index) == 1:
        with t3_c:
            t3_c2 = st.columns(7)
            for i in q.loc[index].values:
                for j,k in zip(i[2:],range(0,len(t3_c2),2)):
                    with t3_c2[k]:
                        k = q.loc[index].columns[k//2 + 2]
                        if j :
                            barcode_image = generate_qrcode(convert_string_to_special(j.upper()))
                            st.image(barcode_image, caption=k, use_column_width=True)
    elif len(index) > 1:
        with t3_c:                        
            st.info('QRcode는 한 개씩만 생성됩니다')