import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the pre-trained machine learning model
model = joblib.load('Regression_model.pkl')  # Replace with the actual path to your model file

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
        st.write("Click the button to open the House Price Prediction GUI")
        if st.button("Open House Price Prediction"):
            st.markdown("<iframe src='https://github.com/RameshMisale/NexTurnAI/blob/main/house_price_prediction.html' width='800' height='600'></iframe>", unsafe_allow_html=True)

    with col2:
        st.subheader("Case 2")
        st.write("Add the content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

    with col3:
        st.subheader("Case 3")
        st.write("Add the content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

# Create a separate Streamlit page for House Price Prediction GUI
if st.url == "https://your-app-url.com/house_price_prediction":
    st.title("House Price Prediction")

    # Create input fields for user input
    sqft = st.number_input("SqFt", min_value=0)
    bedrooms = st.number_input("Bedrooms", min_value=0)
    bathrooms = st.number_input("Bathrooms", min_value=0)
    offers = st.number_input("Offers", min_value=0)
    brick = st.checkbox("Brick")
    neighborhood = st.selectbox("Neighborhood", ["Neighborhood A", "Neighborhood B", "Neighborhood C"])

    if st.button("Predict Price"):
        # Prepare the input data for prediction
        input_data = [sqft, bedrooms, bathrooms, offers, int(brick), neighborhood]

        # Make the prediction using the model
        predicted_price = model.predict([input_data])[0]

        # Display the predicted price
        st.subheader("Predicted Price:")
        st.write(f"${predicted_price:,.2f}")

# Rest of your code...
