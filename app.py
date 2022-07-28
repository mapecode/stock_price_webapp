import yfinance as yf
import streamlit as st

from config import TICKER, PERIOD, START_DATE, END_DATE

st.write("""
# Simple Stock Price App
Ticker: {}
""".format(TICKER))

#define the ticker symbol
tickerSymbol = TICKER
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period=PERIOD, start=START_DATE, end=END_DATE)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing price
"""
)
st.line_chart(tickerDf.Close)


st.write("""
## Volume
"""
)
st.line_chart(tickerDf.Volume)