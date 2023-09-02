import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

st.title("About Litter Locator")
st.write("Did you know that in the USA, there are more than 50 billion pieces of litter along roads and waterways? This is why we present Litter Locator. Litter Locator is an innovative solution to the problem of urban littering. The main aim of Litter Locator is to bring together a community of people who share the common goal of promoting cleaner and healthier surroundings. The website has two key features - users can report and locate litter. ")

st.header("Our goal")


st.sidebar.success('test')
