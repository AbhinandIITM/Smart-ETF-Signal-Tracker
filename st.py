import streamlit as st
import pandas as pd


data = pd.read_csv("latest_etf_data.csv", index_col=0, parse_dates=True)

st.title("Smart ETF Signal Tracker - Live Data")
st.line_chart(data)
