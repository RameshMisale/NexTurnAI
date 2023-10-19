import streamlit as st
from PIL import Image

# Set page title and company logo
st.set_page_config(
    page_title="Interactive Company App",
    page_icon=":rocket:",
    layout="wide"
)
# Open the image file
image = Image.open("Linkedin Banner.png")

# Get the dimensions of the image
width, height = image.size

# Calculate the desired width (in this example, 500 pixels)
desired_width = 500

# Add a title and description
st.title("Welcome to Your Interactive Company App!")
st.write("Explore different cases and navigate to specific links.")


# Case buttons
if st.button("Case One"):
    st.markdown("[Link to Case One](https://innodataengineers.wordpress.com)")

 

if st.button("Case Two"):
    st.markdown("[Link to Case Two](https://www.example.com/case2)")

 

if st.button("Case Three"):
    st.markdown("[Link to Case Three](https://www.example.com/case3)")

 

# Add a fun fact
st.sidebar.header("Fun Fact")
st.sidebar.write("Did you know? Streamlit is an amazing tool for creating interactive web applications with Python!")

 

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")
