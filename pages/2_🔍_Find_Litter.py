import streamlit as st
import pandas as pd
# reported_locations = pd.DataFrame(columns=["Location Name", "Description", "Latitude", "Longitude"])

st.title("Find Litter")
st.write("Search for litter polluted areas near you")
# st.map(reported_locations)

locator = Nominatim(user_agent= "myGeocoder")
address = st.text_input("Address")
search_radius = st.slider("Search Radius (kilometers)", min_value=1, max_value=100, step=1, value=10)

if st.button("Search"):
  location = geolocator.geocode(address)
  st.write(f'{location.latitude}, {location, longitude}')
