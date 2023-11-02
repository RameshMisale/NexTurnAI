import streamlit as st
import joblib

# Load the pre-trained machine learning model
model = joblib.load('Regression_model.pkl')  # Replace with the actual path to your model file

# Set page title and company logo
st.set_page_config(
    page_title="House Price Prediction",
    page_icon=":house:",
    layout="wide"
)

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
