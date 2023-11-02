import streamlit as st
import joblib

st.title("House Price Prediction")

# Create input fields for user input
price = st.number_input("Price")
sqft = st.number_input("SqFt")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
offers = st.number_input("Offers")
brick = st.checkbox("Brick")
neighborhood = st.selectbox("Neighborhood", ["Neighborhood A", "Neighborhood B", "Neighborhood C"])

if st.button("Predict Price"):
    # Load your pre-trained regression model
    model = joblib.load('Regression_model.pkl')
    # Prepare input data for prediction
    input_data = [price, sqft, bedrooms, bathrooms, offers, int(brick), neighborhood]
    # Make the prediction
    predicted_price = model.predict([input_data])[0]
    st.write(f"Predicted Price: ${predicted_price:,.2f}")
