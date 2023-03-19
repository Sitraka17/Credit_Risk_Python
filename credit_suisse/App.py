import pandas as pd
import numpy as np
#!pip install yfinance
import streamlit as st
import yfinance as finance
#chart_data = pd.DataFrame(
#    np.random.randn(20, 3),
#    columns=['a', 'b', 'c'])
#st.line_chart(chart_data)


import streamlit as st
import matplotlib.pyplot as plt

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([1, 2, 3, 4, 5]) 

st.pyplot(fig)
