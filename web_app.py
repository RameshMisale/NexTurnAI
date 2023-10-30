import streamlit as st

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
# image = Image.open("Logo.png")

# Get the dimensions of the image
# width, height = image.size

# Calculate the desired width (in this example, 500 pixels)
desired_width = 50

# Add a title and description
# st.image(image, width=desired_width, use_column_width=True)
st.title("Welcome to NexTurn AI Project!")
st.write("Explore different cases and navigate to specific links.")

# Create a horizontal layout container using custom CSS
st.markdown('<div class="container">')

# Create tabs for Images, Videos, and Audios
tabs = st.tabs(["Images", "Videos", "Audios"])

if tabs == "Images":
    st.markdown('<div class="images-box">Images</div>', unsafe_allow_html=True)
    st.title("Image Section")
    # Placeholder for images or content
elif tabs == "Videos":
    st.markdown('<div class="videos-box">Videos</div>', unsafe_allow_html=True)
    st.title("Video Section")
    # Placeholder for videos or content
else:
    st.markdown('<div class="audios-box">Audios</div>', unsafe_allow_html=True)
    st.title("Audio Section")
    # Placeholder for audios or content

# Close the horizontal layout container
st.markdown('</div>')

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
