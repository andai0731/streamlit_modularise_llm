import streamlit as st
from core import query_result

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is this document about?')
    submitted = st.form_submit_button('Submit')
    
    if submitted:
        st.info(query_result(text))