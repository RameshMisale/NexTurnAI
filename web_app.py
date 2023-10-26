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
            background-color: rgba(0, 0, 0, 0.8); /* Semi-transparent black background */
            color: white; /* Text color */
            background-image: url('https://raw.githubusercontent.com/RameshMisale/NexTurnAI/main/background.jpg'); /* Background image */
            background-size: cover;
            background-attachment: fixed;
            filter: brightness(70%); /* Decrease brightness to 70% */
        }}
        .container {{
            display: flex;
            flex-direction: row;
        }}
        .content {{
            flex: 1; /* Allow content to take remaining space */
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Open the image file (logo)
logo = Image.open("Logo.png")

# Get the dimensions of the logo image
logo_width, logo_height = logo.size

# Calculate the desired width and height for the logo (adjust as needed)
desired_logo_width = 150
desired_logo_height = int(logo_height * (desired_logo_width / logo_width))

# Add the logo in the top left corner
st.image(logo, width=desired_logo_width, height=desired_logo_height, use_container_width=False)

# Add a title and description
st.title("Welcome to NexTurn AI Project!")
st.write("Explore different cases and navigate to specific links.")

# Create a horizontal layout container using custom CSS
st.markdown('<div class="container">')

# Case: Images
st.markdown('<div class="images-box">Images</div>', unsafe_allow_html=True)
st.markdown("Image 1")
st.markdown("[Link to Image 1](https://innodataengineers.wordpress.com)")
st.markdown("Image 2")
st.markdown("[Link to Image 2](https://www.example.com/image2)")
st.markdown("Image 3")
st.markdown("[Link to Image 3](https://www.example.com/image3)")

# Case: Videos
st.markdown('<div class="images-box">Videos</div>', unsafe_allow_html=True)
st.markdown("Video 1")
st.markdown("[Link to Video 1](https://www.example.com/video1)")
st.markdown("Video 2")
st.markdown("[Link to Video 2](https://www.example.com/video2)")
st.markdown("Video 3")
st.markdown("[Link to Video 3](https://www.example.com/video3)")

# Case: Audios
st.markdown('<div class="audios-box">Audios</div>', unsafe_allow_html=True)
st.markdown("Audio 1")
st.markdown("[Link to Audio 1](https://www.example.com/audio1)")
st.markdown("Audio 2")
st.markdown("[Link to Audio 2](https://www.example.com/audio2)")
st.markdown("Audio 3")
st.markdown("[Link to Audio 3](https://www.example.com/audio3)")

# Close the horizontal layout container
st.markdown('</div>')

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
