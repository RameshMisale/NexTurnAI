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
            background-color: white; /* White background for the entire app */
        }}
        .images-box {{
            background-color: #FFFF00; /* Yellow background for Images box */
            padding: 10px;
            border-radius: 5px;
        }}
        .videos-box {{
            background-color: #FF0000; /* Red background for Videos box */
            padding: 10px;
            border-radius: 5px;
        }}
        .audios-box {{
            background-color: #0000FF; /* Blue background for Audios box */
            padding: 10px;
            border-radius: 5px;
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
    st.markdown(
        """
        <div class="images-box">
        <h3>Images</h3>
        <p>Image 1</p>
        <p><a href="https://innodataengineers.wordpress.com">Link to Image 1</a></p>
        <p>Image 2</p>
        <p><a href="https://www.example.com/image2">Link to Image 2</a></p>
        <p>Image 3</p>
        <p><a href="https://www.example.com/image3">Link to Image 3</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Case: Videos
with col2:
    st.markdown(
        """
        <div class="videos-box">
        <h3>Videos</h3>
        <p>Video 1</p>
        <p><a href="https://www.example.com/video1">Link to Video 1</a></p>
        <p>Video 2</p>
        <p><a href="https://www.example.com/video2">Link to Video 2</a></p>
        <p>Video 3</p>
        <p><a href="https://www.example.com/video3">Link to Video 3</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Case: Audios
with col3:
    st.markdown(
        """
        <div class="audios-box">
        <h3>Audios</h3>
        <p>Audio 1</p>
        <p><a href="https://www.example.com/audio1">Link to Audio 1</a></p>
        <p>Audio 2</p>
        <p><a href="https://www.example.com/audio2">Link to Audio 2</a></p>
        <p>Audio 3</p>
        <p><a href="https://www.example.com/audio3">Link to Audio 3</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")
