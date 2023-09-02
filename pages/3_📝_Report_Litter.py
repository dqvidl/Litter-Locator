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
    ('Drop pin on map', 'Address', 'picture'))

st.write('You selected:', option)

if option == "Address":
  address = st.text_input("Address")
