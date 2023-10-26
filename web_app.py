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
            background-image: url('background.jpg'); /* Background image */
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Arial', sans-serif; /* Custom font */
        }}
        .container {{
            display: flex;
            flex-direction: row;
        }}
        .box {{
            background-color: #ffffff; /* White background color */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Shadow effect */
            margin-right: 20px;
        }}
        .box a {{
            text-decoration: none;
            color: #333; /* Dark text color */
            font-weight: bold;
        }}
        .box a:hover {{
            color: #555; /* Hover effect color */
        }}
        .box h3 {{
            color: #555; /* Section title color */
            margin-bottom: 10px;
            font-size: 24px;
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

# Create a horizontal layout container using custom CSS
st.markdown('<div class="container">')

# Case: Images
st.markdown('<div class="box">')
st.markdown('<h3>Images</h3>', unsafe_allow_html=True)
st.markdown("Image 1")
st.markdown("[Link to Image 1](https://innodataengineers.wordpress.com)")
st.markdown("Image 2")
st.markdown("[Link to Image 2](https://www.example.com/image2)")
st.markdown("Image 3")
st.markdown("[Link to Image 3](https://www.example.com/image3)")
st.markdown('</div>')

# Case: Videos
st.markdown('<div class="box">')
st.markdown('<h3>Videos</h3>', unsafe_allow_html=True)
st.markdown("Video 1")
st.markdown("[Link to Video 1](https://www.example.com/video1)")
st.markdown("Video 2")
st.markdown("[Link to Video 2](https://www.example.com/video2)")
st.markdown("Video 3")
st.markdown("[Link to Video 3](https://www.example.com/video3)")
st.markdown('</div>')

# Case: Audios
st.markdown('<div class="box">')
st.markdown('<h3>Audios</h3>', unsafe_allow_html=True)
st.markdown("Audio 1")
st.markdown("[Link to Audio 1](https://www.example.com/audio1)")
st.markdown("Audio 2")
st.markdown("[Link to Audio 2](https://www.example.com/audio2)")
st.markdown("Audio 3")
st.markdown("[Link to Audio 3](https://www.example.com/audio3)")
st.markdown('</div>')

# Close the horizontal layout container
st.markdown('</div>')

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
