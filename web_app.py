import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo and title with an increased size
st.image("Logo.png", width=400, use_column_width=False)  # Increase the width value to adjust the logo size
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs1, tabs2, tabs3 = st.tabs(["Case 1", "Case 2", "Case 3"])

with tabs1:
    st.write("Content for Case 1")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.subheader("Details for Case 1")
        st.write("This is the content for Case 1.")
        st.markdown("You can add more content here.")
 
    with col2:
        st.markdown("<a href='https://your-case1-link.com' target='_blank'>Open Case 1</a>", unsafe_allow_html=True)

with tabs2:
    st.write("Content for Case 2")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.subheader("Details for Case 2")
        st.write("This is the content for Case 2.")
        st.markdown("You can add more content here.")
 
    with col2:
        st.markdown("<a href='https://your-case2-link.com' target='_blank'>Open Case 2</a>", unsafe_allow_html=True)

with tabs3:
    st.write("Content for Case 3")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.subheader("Details for Case 3")
        st.write("This is the content for Case 3.")
        st.markdown("You can add more content here.")
 
    with col2:
        st.markdown("<a href='https://your-case3-link.com' target='_blank'>Open Case 3</a>", unsafe_allow_html=True)
