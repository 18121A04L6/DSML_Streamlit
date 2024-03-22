import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')
code = '''def name():
    print("Hello, Litheesh!")'''
st.code(code, language='python')