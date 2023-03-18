#Try to do a streamlit app ? 
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Credit Suisse Stock Price Evolution")

# Define stock symbol
symbol = 'CS'

# Get stock data from Yahoo Finance
data = yf.download(symbol, period='max')

# Plot stock price evolution
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data['Close'])
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title(f'{symbol} Stock Price Evolution')
st.pyplot(fig)
