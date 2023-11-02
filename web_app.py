import streamlit as st
import joblib

# Set page title and company logo
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="wide"
)

# Logo and title with an increased size
st.image("Logo.png", width=400, use_column_width=False)
st.title("Welcome to House Price Prediction")

# Create input fields for features
sqft = st.number_input("Square Footage", min_value=100, max_value=10000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10)
offers = st.number_input("Number of Offers", min_value=0, max_value=10)
brick = st.checkbox("Brick Exterior")
neighborhood = st.selectbox("Neighborhood", ["Neighborhood A", "Neighborhood B", "Neighborhood C"])

# Load your pre-trained regression model
model = joblib.load('Regression_model.pkl')

# Button to trigger the prediction
if st.button("Get Price Prediction"):
    # Prepare input data for prediction
    input_data = [sqft, bedrooms, bathrooms, offers, int(brick), neighborhood]
    # Make the prediction
    predicted_price = model.predict([input_data])[0]
    st.write(f"Predicted Price: ${predicted_price:,.2f}")

# Footer
st.markdown("---")
st.write("Thank you for using our House Price Prediction tool!")
