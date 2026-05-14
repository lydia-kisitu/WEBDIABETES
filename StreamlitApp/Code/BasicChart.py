import streamlit as st

# Title
st.title('My Streamlit App')

# Sidebar
sidebar_option = st.sidebar.selectbox('Select Option', ['Option 1', 'Option 2'])

# Display data
st.write(f'Selected option: {sidebar_option}')

# Plotting a chart
import numpy as np

chart_data = np.random.randn(20, 3)
st.line_chart(chart_data)

#import pandas as pd
import matplotlib.pyplot as plt
plt.scatter '[salary-data['yearexperienced'],salary-data['salary'])
