import streamlit as st
from PIL import Image

# Set page title and company logo
st.set_page_config(
    page_title="NexTurnAI Project",
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
    st.header("Case One (Images)")
    st.image("image_example.jpg", width=300)
    st.markdown("[Link to Case One](https://innodataengineers.wordpress.com)")

# Case Two: Videos
with col2:
    st.header("Case Two (Videos)")
    st.video("video_example.mp4")
    st.markdown("[Link to Case Two](https://www.example.com/case2)")

# Case Three: Audios
with col3:
    st.header("Case Three (Audios)")
    st.audio("audio_example.mp3")
    st.markdown("[Link to Case Three](https://www.example.com/case3)")

# Add a fun fact
st.sidebar.header("Fun Fact")
st.sidebar.write("Did you know? Streamlit is an amazing tool for creating interactive web applications with Python!")

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")
