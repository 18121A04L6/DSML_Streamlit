import yfinance as yf
import streamlit as st
import datetime

stock=st.text_input("Company",value='NVDA')
st.header('Stock Price Analysis')
st.write("Currently Analysing: ",stock)
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", datetime.date(2024, 2, 22))

with col2:
    end_date = st.date_input("End Date", datetime.date(2024, 3, 22))
# get historical market data
data = yf.Ticker(stock)
hist = data.history(period="1d", start=start_date, end=end_date)
st.dataframe(hist)
st.header('Closing Cost trend')
st.line_chart(hist['Close'])
st.header('Volume trend')
st.bar_chart(hist['Volume'])