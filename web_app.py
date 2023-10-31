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
tabs = st.tabs(["Case 1", "Case 2", "Case 3"])

if tabs == "Case 1":
    st.write("Content for Case 1")

    # Display cat image under Case 1 (use the local file path)
    st.image("cat.jpg", use_column_width=True)
    st.subheader("Cat")

    # Create columns for content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Details for Case 1")
        st.write("This is the content for Case 1.")
        st.markdown("You can add more content here.")

    with col2:
        # Open a new tab with HTML link
        st.markdown("<a href='https://your-case1-link.com' target='_blank'>Open Case 1</a>", unsafe_allow_html=True)

elif tabs == "Case 2":
    st.write("Content for Case 2")

    # Display dog image under Case 2 (use the local file path)
    st.image("dog.jpg", use_column_width=True)
    st.subheader("Dog")

    # Create columns for content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Details for Case 2")
        st.write("This is the content for Case 2.")
        st.markdown("You can add more content here.")

    with col2:
        # Open a new tab with HTML link
        st.markdown("<a href='https://your-case2-link.com' target='_blank'>Open Case 2</a>", unsafe_allow_html=True)

elif tabs == "Case 3":
    st.write("Content for Case 3")

    # Display owl image under Case 3 (use the local file path)
    st.image("owl.jpg", use_column_width=True)
    st.subheader("Owl")

    # Create columns for content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Details for Case 3")
        st.write("This is the content for Case 3.")
        st.markdown("You can add more content here.")

    with col2:
        # Open a new tab with HTML link
        st.markdown("<a href='https://your-case3-link.com' target='_blank'>Open Case 3</a>", unsafe_allow_html=True)
