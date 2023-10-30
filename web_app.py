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
desired_width = 50

# Add a title and description
st.image(image, width=desired_width, use_column_width=True)
st.title("Welcome to NexTurn AI Project!")
st.write("Explore different cases and navigate to specific links.")

# Create a horizontal layout container using custom CSS
st.markdown('<div class="container">')

# Create tabs for Images and Videos
tabs = st.tabs(["Images", "Videos"])

if tabs == "Images":
    st.markdown('<div class="images-box">Images</div>', unsafe_allow_html=True)
    st.title("Image Section")
    st.markdown("Image 1")
    st.markdown("[Link to Image 1](https://innodataengineers.wordpress.com)")
    st.markdown("Image 2")
    st.markdown("[Link to Image 2](https://www.example.com/image2)")
    st.markdown("Image 3")
    st.markdown("[Link to Image 3](https://www.example.com/image3)")

elif tabs == "Videos":
    st.markdown('<div class="videos-box">Videos</div>', unsafe_allow_html=True)
    st.title("Video Section")
    st.markdown("Video 1")
    st.markdown("[Link to Video 1](https://www.example.com/video1)")
    st.markdown("Video 2")
    st.markdown("[Link to Video 2](https://www.example.com/video2)")
    st.markdown("Video 3")
    st.markdown("[Link to Video 3](https://www.example.com/video3)")

# Close the horizontal layout container
st.markdown('</div>')

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
