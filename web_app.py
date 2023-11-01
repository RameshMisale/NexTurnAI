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
 
# Create a radio button for selecting tabs
selected_tab = st.radio("Select a tab:", ["Images", "Videos", "Audios"])
 
# Create columns for content
col1, col2, col3 = st.columns(3)
 
# Add content based on the selected tab
if selected_tab == "Images":
    st.subheader("Images Cases")
 
    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Images Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
    with col2:
        st.subheader("Case 2")
        st.write("You can add content here for Images Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
    with col3:
        st.subheader("Case 3")
        st.write("You can add content here for Images Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
elif selected_tab == "Videos":
    st.subheader("Videos Cases")
 
    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Videos Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
    with col2:
        st.subheader("Case 2")
        st.write("You can add content here for Videos Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
    with col3:
        st.subheader("Case 3")
        st.write("You can add content here for Videos Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
elif selected_tab == "Audios":
    st.subheader("Audios Cases")
 
    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Audios Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
    with col2:
        st.subheader("Case 2")
        st.write("You can add content here for Audios Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
 
    with col3:
        st.subheader("Case 3")
        st.write("You can add content here for Audios Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
