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

# Create tabs for cases
tabs1, tabs2, tabs3 = st.tabs(["Images", "Videos", "Audios"])
with tabs1:
    st.write("Content for image Cases")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1")
        st.write("Click the button to open the House Price Prediction page")
        if st.button("Open House Price Prediction"):
            # Open the House Price Prediction HTML page in a new tab
            st.markdown("<a href='house_price_prediction.html' target='_blank'>Open House Price Prediction</a>", unsafe_allow_html=True)

    with col2:
        st.subheader("Case 2")
        st.write("Add the content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

    with col3:
        st.subheader("Case 3")
        st.write("Add the content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

# Rest of your code...
