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
    st.header("Image 1")
    st.image("image_example_1.jpg", width=300)
    st.markdown("[Link to Image 1](https://innodataengineers.wordpress.com)")

# Case Two: Images
with col2:
    st.header("Image 2")
    st.image("image_example_2.jpg", width=300)
    st.markdown("[Link to Image 2](https://www.example.com/image2)")

# Case Three: Images
with col3:
    st.header("Image 3")
    st.image("image_example_3.jpg", width=300)
    st.markdown("[Link to Image 3](https://www.example.com/image3)")

# Case Four: Videos
with col1:
    st.header("Video 1")
    st.video("video_example_1.mp4")
    st.markdown("[Link to Video 1](https://www.example.com/video1)")

# Case Five: Videos
with col2:
    st.header("Video 2")
    st.video("video_example_2.mp4")
    st.markdown("[Link to Video 2](https://www.example.com/video2)")

# Case Six: Videos
with col3:
    st.header("Video 3")
    st.video("video_example_3.mp4")
    st.markdown("[Link to Video 3](https://www.example.com/video3)")

# Case Seven: Audios
with col1:
    st.header("Audio 1")
    st.audio("audio_example_1.mp3")
    st.markdown("[Link to Audio 1](https://www.example.com/audio1)")

# Case Eight: Audios
with col2:
    st.header("Audio 2")
    st.audio("audio_example_2.mp3")
    st.markdown("[Link to Audio 2](https://www.example.com/audio2)")

# Case Nine: Audios
with col3:
    st.header("Audio 3")
    st.audio("audio_example_3.mp3")
    st.markdown("[Link to Audio 3](https://www.example.com/audio3)")

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")
