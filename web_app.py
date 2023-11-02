import streamlit as st
import pickle

# Load the machine learning model pickle file
model_path = "Regression_model.pkl"
model = pickle.load(open(model_path, "rb"))

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

# Create a function to predict the price of a house
def predict_price(price, sqft, bedrooms, bathrooms, offers, brick, neighborhood):

    # Preprocess the input data
    data = {
        "Price": price,
        "SqFt": sqft,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Offers": offers,
        "Brick": brick,
        "Neighborhood": neighborhood
    }

    # Make a prediction
    prediction = model.predict([data])

    # Return the prediction
    return prediction[0]

# Add input fields for both Images and Videos tabs
with tabs1:
    st.write("Content for image Cases")
    price1 = st.number_input("Price - Images")
    sqft1 = st.number_input("SqFt - Images")
    bedrooms1 = st.number_input("Bedrooms - Images")
    bathrooms1 = st.number_input("Bathrooms - Images")
    offers1 = st.number_input("Offers - Images")
    brick1 = st.checkbox("Brick - Images")
    neighborhood1 = st.text_input("Neighborhood - Images")

with tabs2:
    st.write("Content for Video Cases")
    price2 = st.number_input("Price - Videos")
    sqft2 = st.number_input("SqFt - Videos")
    bedrooms2 = st.number_input("Bedrooms - Videos")
    bathrooms2 = st.number_input("Bathrooms - Videos")
    offers2 = st.number_input("Offers - Videos")
    brick2 = st.checkbox("Brick - Videos")
    neighborhood2 = st.text_input("Neighborhood - Videos")

# Button to predict price
if st.button("Predict Price"):

    if tabs1:
        price = price1
        sqft = sqft1
        bedrooms = bedrooms1
        bathrooms = bathrooms1
        offers = offers1
        brick = brick1
        neighborhood = neighborhood1
    elif tabs2:
        price = price2
        sqft = sqft2
        bedrooms = bedrooms2
        bathrooms = bathrooms2
        offers = offers2
        brick = brick2
        neighborhood = neighborhood2

    # Make the prediction
    prediction = predict_price(price, sqft, bedrooms, bathrooms, offers, brick, neighborhood)

    # Display the prediction to the user
    st.write("Predicted price: ${:.2f}".format(prediction))
