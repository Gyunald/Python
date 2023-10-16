import streamlit as st
from fractions import Fraction

col1, col2 = st.columns([1,1])

def output_1():
    return \
            st.write('---'),\
            st.write('D',round(drill,2)),\
            st.write('T',round(tap_pi,3)),\
            st.write('P',round(pitch,3)),\
            st.write('S',int(rpm),'F',feed),\

tap = col1.text_input("탭 규격",placeholder='ex) 1-8, 7/8-9')
rpm = col1.text_input("RPM",value=100)

col1.write('---')
decimal_number = col1.number_input('소수를 분수로 변환',value=None)

if decimal_number:
    분수 = Fraction(decimal_number).limit_denominator()
    분자 = 분수.numerator
    분모 = 분수.denominator
    col1.write(분수)

col1.write('---')
thread = 0.6134
나사산 =  col1.number_input('UNC 나사', value=None)
직경 = col1.number_input('직경', value=None)
if 나사산 and 직경:
    피치 =  25.4 / 나사산
    나사산높이 = (thread*피치) * 2
    X = round(직경-나사산높이,2)
    col1.write(f"""
    외경  {직경} \n
    내경  {X} \n
    P{int(round(나사산높이/2,4)*1000)} F{피치}
    """)

with col2:
    try:
        if '/' in tap :
            numerator = int(tap[:tap.index('/')])
            denominator = int(tap[tap.index('/')+1 : tap.index('-')])
            tap_thread = int(tap[tap.index('-')+1:])
            tap_pi = (numerator / denominator) * 25.4
            drill = (numerator / denominator) * 25.4 - (25.4 / tap_thread)
            pitch = 25.4 / tap_thread
            feed = round(int(rpm)*pitch,3)
            output_1()
            
        else:  
            integer = int(tap[:tap.index('-')])
            tap_thread = int(tap[tap.index('-')+1:])
            tap_pi = integer * 25.4
            drill = (integer * 25.4) - (25.4 / tap_thread)
            pitch = 25.4 / tap_thread
            feed = round(int(rpm)*pitch,2)
            output_1()

    except ValueError:
        st.warning('입력 확인')
