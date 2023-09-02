import streamlit as st
import pandas as pd
# from geopy.geocoders import Nominatim

st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

st.header("Find Litter")
st.write("Search for litter polluted areas near you")

# locator = Nominatim(user_agent= "myGeocoder")
address = st.text_input("Address")
search_radius = st.slider("Search Radius (kilometers)", min_value=1, max_value=100, step=1, value=10)

# if st.button("Search"):
#   location = geolocator.geocode(address)
#   st.write(f'{location.latitude}, {location.longitude}')
