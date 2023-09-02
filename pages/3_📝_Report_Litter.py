import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

st.header("Report Litter")
st.write("Report litter polluted areas")

option = st.selectbox(
    'How would you like to report a littered area?',
    ('Choose','Drop pin on map', 'Address'))

st.write('You selected:', option)


if option == "Address":
  address = st.text_input("Address")
elif option == 'Drop pin on map':
  st.write("hello world")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [43.46, -80.52],
    columns=['lat', 'lon'])

st.map(df)
