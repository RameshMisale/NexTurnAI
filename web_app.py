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
tabs = st.tabs(["Images", "Videos", "Audios"])

# Iterate over the tabs
for i in range(len(tabs)):

    # Get the tab name
    tab_name = tabs[i]

    # Create a tab item
    with st.tab_item(tab_name + " Cases"):

        # Create columns for content
        col1, col2, col3 = st.columns(3)

        # Add content to the columns
        with col1:
            st.subheader("Case 1")
            st.write("This is the content for {} Case 1.".format(tab_name))
            st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

        with col2:
            st.subheader("Case 2")
            st.write("You can add content here for {} Case 2.".format(tab_name))
            st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

        with col3:
            st.subheader("Case 3")
            st.write("You can add content here for {} Case 3.".format(tab_name))
            st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

 
