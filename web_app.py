
import streamlit as st

from PIL import Image
 
# Set page title and company logo

st.set_page_config(

    page_title="NexTurn AI Project",

    page_icon=":rocket:",

    layout="wide"

)
 
# Define the background color and text brightness using CSS

st.markdown(

    f"""

    <style>

        .stApp {{

            background-color: rgba(0, 0, 0, 0.8); /* Semi-transparent black background */

            color: white; /* Text color */

            background-image: url('https://raw.githubusercontent.com/RameshMisale/NexTurnAI/main/background.jpg'); /* Background image */

            background-size: cover;

            background-attachment: fixed;

            filter: brightness(80%); /* Reduced background brightness to 80% */

        }}

        .container {{

            display: flex;

            flex-direction: row;

        }}

        .images-box {{

            background-color: blue; /* blue background color */

            padding: 10px;

            border-radius: 10px;

            margin-right: 10px;

        }}

        .videos-box {{

            background-color: red; /* red background color */

            padding: 10px;

            border-radius: 10px;

            margin-right: 10px;

        }}

        .audios-box {{

            background-color: purple; /* purple background color */

            padding: 10px;

            border-radius: 10px;

        }}

        .stMarkdown {{

            filter: brightness(200%); /* Increased text brightness to 200% */

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

desired_width = 50
 
# Add a title and description

st.image(image, width=desired_width, use_column_width=True)

st.title("Welcome to NexTurn AI Project!")

st.write("Explore different cases and navigate to specific links.")
 
# Create a horizontal layout container using custom CSS

#st.markdown('<div class="container">')
 
# Case: Images

st.markdown('<div class="images-box">Images</div>', unsafe_allow_html=True)

st.title("Image Section")

st.markdown("Image 1")

st.markdown("[Link to Image 1](https://innodataengineers.wordpress.com)")

st.markdown("Image 2")

st.markdown("[Link to Image 2](https://www.example.com/image2)")

st.markdown("Image 3")

st.markdown("[Link to Image 3](https://www.example.com/image3)")
 
# Case: Videos

st.markdown('<div class="videos-box">Videos</div>', unsafe_allow_html=True)

st.title("Video Section")

st.markdown("Video 1")

st.markdown("[Link to Video 1](https://www.example.com/video1)")

st.markdown("Video 2")

st.markdown("[Link to Video 2](https://www.example.com/video2)")

st.markdown("Video 3")

st.markdown("[Link to Video 3](https://www.example.com/video3)")
 
# Case: Audios

st.markdown('<div class="audios-box">Audios</div>', unsafe_allow_html=True)

st.title("Audio Section")

st.markdown("Audio 1")

st.markdown("[Link to Audio 1](https://www.example.com/audio1)")

st.markdown("Audio 2")

st.markdown("[Link to Audio 2](https://www.example.com/audio2)")

st.markdown("Audio 3")

st.markdown("[Link to Audio 3](https://www.example.com/audio3)")
 
# Close the horizontal layout container

#st.markdown('</div>')
 
# Footer

st.markdown("---")

st.write("Thank you for visiting...!!")

# [Monday 15:02] Ramesh Misale
# import streamlit as st
 
# # Set page title and company logo

# st.set_page_config(

#     page_title="NexTurn AI Project",

#     page_icon=":rocket:",

#     layout="wide"

# )
 
# # Logo

# st.image("Logo.jpg")

# st.title("Welcome to NexTurn AI Project")
 
# # Create tabs for cases

# tabs = st.tabs(["Case 1", "Case 2", "Case 3"])
 
# if tabs == "Case 1":

#     st.write("Content for Case 1")
 
#     # Create columns for content

#     col1, col2 = st.columns(2)
 
#     with col1:

#         st.subheader("Details for Case 1")

#         st.write("This is the content for Case 1.")

#         st.markdown("You can add more content here.")
 
#     with col2:

#         # Open a new tab with HTML link

#         st.markdown("<a href='https://your-case1-link.com' target='_blank'>Open Case 1</a>", unsafe_allow_html=True)
 
# elif tabs == "Case 2":

#     st.write("Content for Case 2")
 
#     # Create columns for content

#     col1, col2 = st.columns(2)
 
#     with col1:

#         st.subheader("Details for Case 2")

#         st.write("This is the content for Case 2.")

#         st.markdown("You can add more content here.")
 
#     with col2:

#         # Open a new tab with HTML link

#         st.markdown("<a href='https://your-case2-link.com' target='_blank'>Open Case 2</a>", unsafe_allow_html=True)
 
# elif tabs == "Case 3":

#     st.write("Content for Case 3")
 
#     # Create columns for content

#     col1, col2 = st.columns(2)
 
#     with col1:

#         st.subheader("Details for Case 3")

#         st.write("This is the content for Case 3.")

#         st.markdown("You can add more content here.")
 
#     with col2:

#         # Open a new tab with HTML link

#         st.markdown("<a href='https://your-case3-link.com' target='_blank'>Open Case 3</a>", unsafe_allow_html=True)
