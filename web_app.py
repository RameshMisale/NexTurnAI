import streamlit as st
from PIL import Image

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Define the background color using CSS
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: #000000; /* Black background color */
        }}
        .images-box {{
            background-color: #EED9C7; /* Blue background color */
            padding: 10px;
            border-radius: 10px;
        }}
        .videos-box {{
            background-color: #963939; /* Antique Ruby background color */
            padding: 10px;
            border-radius: 10px;
        }}
        .audios-box {{
            background-color: #8DB051; /* Artichoke Green background color */
            padding: 10px;
            border-radius: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
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

# Case: Images
with col1:
    st.markdown('<div class="images-box">Images</div>', unsafe_allow_html=True)
    st.markdown("Image 1")
    st.markdown("[Link to Image 1](https://innodataengineers.wordpress.com)")
    st.markdown("Image 2")
    st.markdown("[Link to Image 2](https://www.example.com/image2)")
    st.markdown("Image 3")
    st.markdown("[Link to Image 3](https://www.example.com/image3)")

# Case: Videos
with col2:
    st.markdown('<div class="videos-box">Videos</div>', unsafe_allow_html=True)
    st.markdown("Video 1")
    st.markdown("[Link to Video 1](https://www.example.com/video1)")
    st.markdown("Video 2")
    st.markdown("[Link to Video 2](https://www.example.com/video2)")
    st.markdown("Video 3")
    st.markdown("[Link to Video 3](https://www.example.com/video3)")

# Case: Audios
with col3:
    st.markdown('<div class="audios-box">Audios</div>', unsafe_allow_html=True)
    st.markdown("Audio 1")
    st.markdown("[Link to Audio 1](https://www.example.com/audio1)")
    st.markdown("Audio 2")
    st.markdown("[Link to Audio 2](https://www.example.com/audio2)")
    st.markdown("Audio 3")
    st.markdown("[Link to Audio 3](https://www.example.com/audio3)")

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")
