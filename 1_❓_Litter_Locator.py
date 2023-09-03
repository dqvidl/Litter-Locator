import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 


st.title("About Litter Locator")
image = Image.open('environment.jpg')
st.image(image, caption = 'Help reduce littering')
st.write("Did you know that in the United States alone, an astonishing 51 billion pieces of litter are left on the ground every year? This shocking statistic highlights a pervasive issue that not only harms the environment but also degrades the way our communities are presented. After all, no one likes seeing a litter ridden city. In response to this alarming problem, Litter Locator has emerged as a beacon of hope in the battle against litter.  Litter Locator is not just a website; it's a powerful tool for change. By harnessing the collective efforts of concerned citizens, it presents a novel approach to reducing litter. Anyone can use the platform to self-report large quantities of litter in their communities, pinpointing trouble spots that need urgent attention. What sets Litter Locator apart is its ingenious system of mobilizing teams of dedicated cleaners who access the reported locations on the website, swiftly locating and cleaning these litter-ridden areas.  This dynamic synergy between technology and community engagement not only helps to keep our surroundings clean but also fosters a sense of shared responsibility. Litter Locator isn't just cleaning up our streets; it's cleaning up our collective conscience. Join the movement and be a part of the solution. Together, we can make a world with less litter and more beauty.")

st.divider()

with st.container():
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Our goal")
    st.write("At Litter Locator, our overarching goal is to create cleaner, more beautiful, and environmentally responsible communities. We envision a world where litter is no longer a blight on our neighborhoods, parks, and public spaces, and where the idea of a cleaner environment is championed by individuals and communities alike.")

st.divider()
st.header("Report")
st.write("In the reporting section of Litter Locator, we've made it incredibly easy for you to be the catalyst for change in your community. When you come across a littered area that needs attention, simply navigate to our user-friendly reporting interface. Here, you can upload the exact location using GPS coordinates. However, there's more to it. We know that a picture is worth a thousand words, which is why we encourage you to snap a photo of the littered area. These images provide crucial context, helping us understand the extent of the issue and allowing volunteers to prepare accordingly. With your location and photographic evidence, you're not just reporting a problem; you're providing a clear and actionable insight that empowers our community to come together and make a real impact.")

st.divider()
st.header("Find")
st.write("We believe that change requires a collective effort. After a littered area has been reported on our Litter Locator website, the process of finding and addressing the litter becomes a community-driven effort. Once a report is submitted, it is immediately added to our interactive map, pinpointing the exact location for all users to see. Community members, volunteers, and concerned citizens can then take action by referring to the map, selecting a reported area that resonates with them, and organizing clean-up efforts. Our platform serves as a vital communication hub, connecting those who care with the specific areas in need of attention, ensuring that the response to litter reports is swift and effective. Together, we turn reports into action, making a lasting impact on the cleanliness and beauty of our communities.")
