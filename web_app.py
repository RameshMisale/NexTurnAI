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

# Create a sidebar for navigation
with st.sidebar:
    # Add a radio button to select the section
    selected_section = st.radio("Select a Section", ["Images Cases", "Videos Cases", "Audios Cases"])

if selected_section == "Images Cases":
    st.write("Images Cases")

    # Create a container for Case 1
    with st.container():
        st.subheader("Case 1")
        st.write("This is the content for Images Case 1.")
        st.markdown("You can add more content here.")

    # Create a container for Case 2
    with st.container():
        st.subheader("Case 2")
        st.write("You can add content here for Images Case 2.")
        st.markdown("Additional information goes here.")

    # Create a container for Case 3
    with st.container():
        st.subheader("Case 3")
        st.write("You can add content here for Images Case 3.")
        st.markdown("More information goes here.")

elif selected_section == "Videos Cases":
    st.write("Videos Cases")

    # Create a container for Case 1
    with st.container():
        st.subheader("Case 1")
        st.write("This is the content for Videos Case 1.")
        st.markdown("You can add more content here.")

    # Create a container for Case 2
    with st.container():
        st.subheader("Case 2")
        st.write("You can add content here for Videos Case 2.")
        st.markdown("Additional information goes here.")

    # Create a container for Case 3
    with st.container():
        st.subheader("Case 3")
        st.write("You can add content here for Videos Case 3.")
        st.markdown("More information goes here.")

elif selected_section == "Audios Cases":
    st.write("Audios Cases")

    # Create a container for Case 1
    with st.container():
        st.subheader("Case 1")
        st.write("This is the content for Audios Case 1.")
        st.markdown("You can add more content here.")

    # Create a container for Case 2
    with st.container():
        st.subheader("Case 2")
        st.write("You can add content here for Audios Case 2.")
        st.markdown("Additional information goes here.")

    # Create a container for Case 3
    with st.container():
        st.subheader("Case 3")
        st.write("You can add content here for Audios Case 3.")
        st.markdown("More information goes here.")
