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
  df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [43.46, -80.52],
    columns=['lat', 'lon'])

  st.map(df)

st.subheader("Please provide an image")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
