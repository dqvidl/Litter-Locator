reported_locations = pd.DataFrame(columns=["Location Name", "Description", "Latitude", "Longitude"])

st.title("Find Litter")
st.write("Search for litter polluted areas near you")
st.map(reported_locations)

locator = Nominatim(user_agent=”myGeocoder”)
location = geolocator.geocode("175 5th Avenue NYC")
search_radius = st.slider("Search Radius (kilometers)", min_value=1, max_value=100, step=1, value=10)
