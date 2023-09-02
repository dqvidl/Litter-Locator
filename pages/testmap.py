import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim


st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

data = []

data.append({
  "Latitude" : 43.46,
  "Longitude" : -80.52
})

st.map(data)
