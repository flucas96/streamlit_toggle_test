import streamlit as st



st.toggle("Switch 1", value=False, key="switch1")


col_left,col_right = st.columns((1,1))
with col_left: 

    st.toggle("Switch left", value=False, key="switch_left")


with col_right:
    st.toggle("Switch right", value=False, key="switch_right")