import streamlit as st
from PIL import Image

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Open the image file
image = Image.open("Logo.png")

# Get the dimensions of the image
width, height = image.size

# Calculate the desired width (in this example, 500 pixels)
desired_width = 500

# Add a title and description
st.image(image, width=desired_width, use_column_width=True)
st.title("Welcome to NexTurn AI Project!")
st.write("Explore different cases and navigate to specific links.")

# Define the layout for the cases
col1, col2, col3 = st.columns(3)

# Case One: Images
with col1:
    st.info("Images")
    st.markdown("Case 1")
    st.markdown("[Image 1](https://innodataengineers.wordpress.com)")
    st.markdown("[Image 2](https://www.example.com/image2)")
    st.markdown("[Image 3](https://www.example.com/image3)")

# Case Two: Videos
with col2:
    st.info("Videos")
    st.markdown("Case 2")
    st.markdown("[Video 1](https://www.example.com/video1)")
    st.markdown("[Video 2](https://www.example.com/video2)")
    st.markdown("[Video 3](https://www.example.com/video3)")

# Case Three: Audios
with col3:
    st.info("Audios")
    st.markdown("Case 3")
    st.markdown("[Audio 1](https://www.example.com/audio1)")
    st.markdown("[Audio 2](https://www.example.com/audio2)")
    st.markdown("[Audio 3](https://www.example.com/audio3)")

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")
