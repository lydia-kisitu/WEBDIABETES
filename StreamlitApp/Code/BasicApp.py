import streamlit as st

# Title
st.title('My First Streamlit App')

# Sidebar
sidebar_option = st.sidebar.selectbox('Select Vechicles', ['Car', 'Bus'])

# Display data
st.write(f'Selected option: {sidebar_option}')

# Inserting a relevant image
if sidebar_option == 'Car':
    st.image('Code\car.jpg', caption='Car')
else:
    st.image('Code\\bus.png', caption='Bus')
