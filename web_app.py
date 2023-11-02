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
tabs1, tabs2, tabs3 = st.tabs(["Images", "Videos", "Audios"])

with tabs1:
    st.write("Content for image Cases")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1 - House Price Prediction")
        st.write("Click the button to open the House Price Prediction page")
        if st.button("Open House Price Prediction"):
            st.write("You are being redirected to the House Price Prediction page.")
            # Redirect to the House Price Prediction page using a link
            st.markdown("[Open House Price Prediction](https://www.example.com/house_price_prediction)", unsafe_allow_html=True)

    # Add content for Case 2 and Case 3 here

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
