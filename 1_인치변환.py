import streamlit as st
import pandas as pd

@st.cache_resource
def Nums():
    return {}

nums = Nums()

if 'nums' not in st.session_state:
    st.session_state.nums = nums

st.title("Inches to Millimeters")

col1, col2, = st.columns([1,1])

with col1:
    num = st.number_input("인치 입력 😎",value=None,format="%f ",) # f뒤에 공백!
    if num:
        nums[num] = num * 25.4
        delete = st.button('DELETE',use_container_width=True)
        clear = st.button('CLEAR',use_container_width=True, type='primary')

        if delete:
            del nums[num]
        if clear :
            nums.clear()
    st.info("""
    ### TOLERANCES 🏈\n
    ##### .0  ± 2.54\n
    ##### .00  ± 0.762\n
    ##### .000  ± 0.254
    """)
    st.link_button('🎲공차 ISO 286', 'https://www.mesys.ch/calc/tolerances.fcgi?lang=ko',use_container_width=True)

with col2:
    df =pd.DataFrame({'inch' : nums.keys(), 'mm' : nums.values()})
    st.dataframe(df.style.format("{:.3f}"),use_container_width=True,hide_index=True)