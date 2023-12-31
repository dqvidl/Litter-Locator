import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim


st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

st.header("Report Litter")
st.write("Report litter polluted areas")

option = st.selectbox(
    'How would you like to report a littered area?',
    ('  ','Drop pin on map', 'Address'))

st.write('You selected:', option)


data = pd.DataFrame(colums=['lat', 'lon'])

if option == "Address":
  address = st.text_input("Address")
  if st.button("Find"):
    if address:
      geolocator = Nominatim(user_agent="address-to-coordinates-converter")
      try:
          location = geolocator.geocode(address)

          if location:
              data += ({location.latitude}, {location.lonitude})
              st.write("Thanks for your input")
          else:
              st.error("Address not found. Please enter a valid address.")
      except Exception as e:
            st.error(f"An error occurred: {str(e)}")

elif option == "Drop pin on map":
  st.map(data)

st.subheader("Picture")

pictureorno = st.selectbox("Would you like to provide photographic evidence of the region?", (' ', 'YES', 'NO'))

if pictureorno == 'YES':
  pictureOption = st.selectbox("Choose:", (' ', 'Choose Photo from Library', 'Take Picture'))
  if pictureOption == 'Take Picture':
    picture = st.camera_input("Take a picture")
    if picture:
      st.image(picture)
  elif pictureOption == 'Choose Photo from Library':
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

st.subheader("Thank you")

