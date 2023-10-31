import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
) 

# Logo and title
st.image("Logo.jpg", width=100, use_column_width=False)
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs1, tabs2, tabs3 = st.tabs(["Images", "Videos", "Audios"])
#st.write(tabs)

if tabs1:
    st.write("Case 1")

    # Display cat image under Case 1 (use the local file path)
    st.image("cat.jpg", use_column_width=True)
    st.subheader("Cat")

    # Create columns for content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Case 1.")
        st.markdown("You can add more content here.")

    with col2:
        st.subheader("Case 2")
        st.write("You can add content here.")
        st.markdown("Additional information goes here.")

    with col3:
        st.subheader("Case 3")
        st.write("You can add content here.")
        st.markdown("More information goes here.")

if tabs2:
    st.write("Case 2")

    # Display dog image under Case 2 (use the local file path)
    st.image("dog.jpg", use_column_width=True)
    st.subheader("Dog")

    # Create columns for content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Case 2.")
        st.markdown("You can add more content here.")

    with col2:
        st.subheader("Case 2")
        st.write("You can add content here.")
        st.markdown("Additional information goes here.")

    with col3:
        st.subheader("Case 3")
        st.write("You can add content here.")
        st.markdown("More information goes here.")

if tabs3:
    st.write("Content for Case 3")

    # Display owl image under Case 3 (use the local file path)
    st.image("owl.jpg", use_column_width=True)
    st.subheader("Owl")

    # Create columns for content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Case 3.")
        st.markdown("You can add more content here.")

    with col2:
        st.subheader("Case 2")
        st.write("You can add content here.")
        st.markdown("Additional information goes here.")

    with col3:
        st.subheader("Case 3")
        st.write("You can add content here.")
        st.markdown("More information goes here.")
