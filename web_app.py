import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo and title with an increased size
st.image("Logo.png", width=400, use_column_width=False)
st.title("Welcome to NexTurn AI Project")

# Create containers for each tab
images_container = st.container()
videos_container = st.container()
audios_container = st.container()

# Create tabs for selecting content
selected_tab = st.radio("Select a tab:", ["Images", "Videos", "Audios"])

# Add content based on the selected tab
if selected_tab == "Images":
    with images_container:
        st.subheader("Images Cases")
        st.subheader("Case 1")
        st.write("This is the content for Images Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

elif selected_tab == "Videos":
    with videos_container:
        st.subheader("Videos Cases")
        st.subheader("Case 1")
        st.write("This is the content for Videos Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

elif selected_tab == "Audios":
    with audios_container:
        st.subheader("Audios Cases")
        st.subheader("Case 1")
        st.write("This is the content for Audios Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
