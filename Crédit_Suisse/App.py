import pandas as pd
import numpy as np
import streamlit as st

#chart_data = pd.DataFrame(
#    np.random.randn(20, 3),
#    columns=['a', 'b', 'c'])
#st.line_chart(chart_data)

import yfinance as yf
import streamlit as st

# Define stock symbol
symbol = 'CS'

# Get stock data from Yahoo Finance
data = yf.download(symbol, period='max')

# Create a dataframe with the closing prices
df = data[['Close']]

# Display the closing prices as a line chart
st.line_chart(df)
