import streamlit as st
from PIL import Image

# Set page title and company logo
st.set_page_config(
    page_title="Beautiful Streamlit Website",
    page_icon=":art:",
    layout="wide"
)

# Define the background style using CSS
st.markdown(
    f"""
    <style>
        .stApp {{
            background: url('background.jpg'); /* Background image */
            background-size: cover;
            background-blur: 10px; /* Blur effect for background */
            color: white; /* Text color */
            font-family: 'Arial', sans-serif; /* Custom font */
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .header {{
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
        }}
        .content {{
            background-color: rgba(0, 0, 0, 0.5); /* Translucent background for content */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Shadow effect */
            text-align: center;
            max-width: 800px;
            margin-bottom: 20px;
        }}
        .box a {{
            text-decoration: none;
            color: #fff; /* Link color */
            font-weight: bold;
        }}
        .box a:hover {{
            color: #ddd; /* Hover effect color */
        }}
        .box h3 {{
            color: #ddd; /* Section title color */
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
st.title("Welcome to Our Beautiful Streamlit Website!")
st.markdown("Explore the amazing content we have to offer.")

# Create a container for the content using custom CSS
st.markdown('<div class="container">')

# Section 1
st.markdown('<div class="content">')
st.markdown('<h3 class="header">Section 1</h3>', unsafe_allow_html=True)
st.markdown("This is the content of Section 1.")
st.markdown("[Link to Section 1](https://example.com/section1)")
st.markdown('</div>')

# Section 2
st.markdown('<div class="content">')
st.markdown('<h3 class="header">Section 2</h3>', unsafe_allow_html=True)
st.markdown("This is the content of Section 2.")
st.markdown("[Link to Section 2](https://example.com/section2)")
st.markdown('</div>')

# Section 3
st.markdown('<div class="content">')
st.markdown('<h3 class="header">Section 3</h3>', unsafe_allow_html=True)
st.markdown("This is the content of Section 3.")
st.markdown("[Link to Section 3](https://example.com/section3)")
st.markdown('</div>')

# Close the container for the content
st.markdown('</div>')

# Footer
st.markdown("---")
st.write("Thank you for visiting our beautiful website!")

# Display images or additional content as needed
