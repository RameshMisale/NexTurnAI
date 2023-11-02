import streamlit as st
import joblib

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
        st.write("Click the button to predict house price")
        if st.button("Open House Price Prediction"):
            st.write("Please enter the details below:")
            sqft = st.number_input("SqFt")
            bedrooms = st.number_input("Bedrooms")
            bathrooms = st.number_input("Bathrooms")
            offers = st.number_input("Offers")
            brick = st.checkbox("Brick")
            neighborhood = st.selectbox("Neighborhood", ["Neighborhood A", "Neighborhood B", "Neighborhood C"])
            if st.button("Get Price Prediction"):
                # Load your pre-trained regression model
                model = joblib.load('Regression_model.pkl')
                # Prepare input data for prediction
                input_data = [sqft, bedrooms, bathrooms, offers, int(brick), neighborhood]
                # Make the prediction
                predicted_price = model.predict([input_data])[0]
                st.write(f"Predicted Price: ${predicted_price:,.2f}")

    with col2:
        st.subheader("Case 2")
        st.write("Add the content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

    with col3:
        st.subheader("Case 3")
        st.write("Add the content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

with tabs2:
    st.write("Content for Video Cases")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Case 1")
        st.write("Add content for Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    with col2:
        st.subheader("Case 2")
        st.write("Add content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    with col3:
        st.subheader("Case 3")
        st.write("Add content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

with tabs3:
    st.write("Content for Audio Cases")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Case 1")
        st.write("Add content for Case 1.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    with col2:
        st.subheader("Case 2")
        st.write("Add content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    with col3:
        st.subheader("Case 3")
        st.write("Add content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
