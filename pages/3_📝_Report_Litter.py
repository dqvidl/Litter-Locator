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

"""
data = []
ACCELERATOR_CENTER = (43.477351051348485, -80.54952878983036)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(ACCELERATOR_CENTER, zoom = 7.5)"""

option = st.selectbox(
    'How would you like to report a littered area?',
    ('Address', 'Drop pin on map'))

st.write('You selected:', option)

if option = address:
  address = st.text_input("Address")
