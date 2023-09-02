import streamlit as st
import pandas as pd

st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

st.header("Report Litter")
st.write("Report litter polluted areas")

address = st.text_input("Address")

