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

# Create tabs for cases
tabs1, tabs2, tabs3 = st.tabs(["Images", "Videos", "Audios"])

if tabs1:
    st.write("Sample Cases")

    # Create columns for content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1")
        st.write("This is the content for Case 1.")
        st.markdown("https://www.example.com", unsafe_allow_html=True)

    with col2:
        st.subheader("Case 2")
        st.write("You can add content here.")
        st.markdown("https://www.example.com", unsafe_allow_html=True)

    with col3:
        st.subheader("Case 3")
        st.write("You can add content here.")
        st.markdown("https://www.example.com", unsafe_allow_html=True)

# if tabs2:
#     st.write("Sample Cases")

#     # Create columns for content
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.subheader("Case 1")
#         st.write("This is the content for Case 2.")
#         st.markdown("You can add more content here.")

#     with col2:
#         st.subheader("Case 2")
#         st.write("You can add content here.")
#         st.markdown("Additional information goes here.")

#     with col3:
#         st.subheader("Case 3")
#         st.write("You can add content here.")
#         st.markdown("More information goes here.")

# if tabs3:
#     st.write("Sample Cases")

#     # Create columns for content
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.subheader("Case 1")
#         st.write("This is the content for Case 3.")
#         st.markdown("You can add more content here.")

    # with col2:
    #     st.subheader("Case 2")
    #     st.write("You can add content here.")
    #     st.markdown("Additional information goes here.")

    # with col3:
    #     st.subheader("Case 3")
    #     st.write("You can add content here.")
    #     st.markdown("More information goes here.")
