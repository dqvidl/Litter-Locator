import streamlit as st
import pandas as pd
import requests
import urllib.parse


st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

st.header("Find Litter")
st.write("Search for litter polluted areas near you")

address = 'Shivaji Nagar, Bangalore, KA 560001'
# address = st.text_input("Address")
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
search_radius = st.slider("Search Radius (kilometers)", min_value=1, max_value=100, step=1, value=10)

if st.button("Search"):
  response = requests.get(url).json()
  location = geolocator.geocode(address)
  st.write(f'{response[0]["lat"]}, {response[0]["lon"]}')
