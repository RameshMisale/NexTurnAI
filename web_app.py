import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo
st.image("Logo.png")
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs = st.tabs(["Case 1", "Case 2", "Case 3"])

if tabs == "Case 1":
    st.write("Content for Case 1")

    # Container for Case 1
    with st.container():
        st.subheader("Details for Case 1")
        st.write("This is the content for Case 1.")
        st.markdown("You can add more content here.")

    # Open a new tab with HTML link
    st.markdown("<a href='https://your-case1-link.com' target='_blank'>Open Case 1</a>", unsafe_allow_html=True)

elif tabs == "Case 2":
    st.write("Content for Case 2")

    # Container for Case 2
    with st.container():
        st.subheader("Details for Case 2")
        st.write("This is the content for Case 2.")
        st.markdown("You can add more content here.")

    # Open a new tab with HTML link
    st.markdown("<a href='https://your-case2-link.com' target='_blank'>Open Case 2</a>", unsafe_allow_html=True)

elif tabs == "Case 3":
    st.write("Content for Case 3")

    # Container for Case 3
    with st.container():
        st.subheader("Details for Case 3")
        st.write("This is the content for Case 3.")
        st.markdown("You can add more content here.")

    # Open a new tab with HTML link
    st.markdown("<a href='https://your-case3-link.com' target='_blank'>Open Case 3</a>", unsafe_allow_html=True)
