import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo and title with an increased size
st.image("Logo.png", width=400, use_column_width=False)  # Adjust the width value
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs = ["Images", "Videos", "Audios"]
selected_tab = st.radio("Select a case type:", tabs)

# Define the content for each tab
if selected_tab == "Images":
    st.subheader("Case 1")
    st.write("This is the content for Images Case 1.")
    st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

elif selected_tab == "Videos":
    st.subheader("Case 2")
    st.write("You can add content here for Videos Case 2.")
    st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

elif selected_tab == "Audios":
    st.subheader("Case 3")
    st.write("You can add content here for Audios Case 3.")
    st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
