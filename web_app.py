import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo and title with an increased size
st.image("Logo.jpg", width=400, use_column_width=False)  # Adjust the width value
st.title("Welcome to NexTurn AI Project")

# Create tabs for sections
tabs = st.tabs(["Images Cases", "Videos Cases", "Audios Cases"])

if tabs == "Images Cases":
    st.write("Images Cases")

    # Create containers for each case
    with st.container():
        with st.container():
            st.subheader("Case 1")
            st.write("This is the content for Images Case 1.")
            st.markdown("You can add more content here.")

        with st.container():
            st.subheader("Case 2")
            st.write("You can add content here for Images Case 2.")
            st.markdown("Additional information goes here.")

        with st.container():
            st.subheader("Case 3")
            st.write("You can add content here for Images Case 3.")
            st.markdown("More information goes here.")

elif tabs == "Videos Cases":
    st.write("Videos Cases")

    # Create containers for each case
    with st.container():
        with st.container():
            st.subheader("Case 1")
            st.write("This is the content for Videos Case 1.")
            st.markdown("You can add more content here.")

        with st.container():
            st.subheader("Case 2")
            st.write("You can add content here for Videos Case 2.")
            st.markdown("Additional information goes here.")

        with st.container():
            st.subheader("Case 3")
            st.write("You can add content here for Videos Case 3.")
            st.markdown("More information goes here.")

elif tabs == "Audios Cases":
    st.write("Audios Cases")

    # Create containers for each case
    with st.container():
        with st.container():
            st.subheader("Case 1")
            st.write("This is the content for Audios Case 1.")
            st.markdown("You can add more content here.")

        with st.container():
            st.subheader("Case 2")
            st.write("You can add content here for Audios Case 2.")
            st.markdown("Additional information goes here.")

        with st.container():
            st.subheader("Case 3")
            st.write("You can add content here for Audios Case 3.")
            st.markdown("More information goes here.")
