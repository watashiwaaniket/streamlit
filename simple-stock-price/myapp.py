import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple  stock Price App
         
Shown are the stock closing price and volume of Google!

""")

#define the ticker symbol
tickerSymbol = 'NVDA'
#get data on this ticker
ticketData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2014-5-31', end='2024-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
