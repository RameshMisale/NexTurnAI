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

# Images tab
with tabs1:
    st.write("Content for image Cases")
    col1, col2, col3 = st.columns(3)

    # Add a "Predict Price" button to the Images tab
    if st.button("Predict Price"):

        # Open a new dialog box with the input fields
        dialog = st.dialog("Predict House Price")

        # Add the input fields to the dialog box
        with dialog:
            price = st.number_input("Price")
            sqft = st.number_input("SqFt")
            bedrooms = st.number_input("Bedrooms")
            bathrooms = st.number_input("Bathrooms")
            offers = st.number_input("Offers")
            brick = st.checkbox("Brick")
            neighborhood = st.text_input("Neighborhood")

            # If the user clicks on the "Predict" button, predict the price of the house
            if st.button("Predict"):

                # Make the prediction
                prediction = predict_price(price, sqft, bedrooms, bathrooms, offers, brick, neighborhood)

                # Display the prediction to the user
                st.write("Predicted price: ${:.2f}".format(prediction))

        # Close the dialog box
        dialog.close()

# Videos tab
with tabs2:
    st.write("Content for Video Cases")
    col1, col2, col3 = st.columns(3)

    # Add a "Predict Price" button to the Videos tab
    if st.button("Predict Price"):

        # Open a new dialog box with the input fields
        dialog = st.dialog("Predict House Price")

        # Add the input fields to the dialog box
        with dialog:
            price = st.number_input("Price")
            sqft = st.number_input("SqFt")
            bedrooms = st.number_input("Bedrooms")
            bathrooms = st.number_input("Bathrooms")
            offers = st.number_input("Offers")
            brick = st.checkbox("Brick")
            neighborhood = st.text_input("Neighborhood")

            # If the user clicks on the "Predict" button, predict the price of the house
            if st.button("Predict"):

                # Make the prediction
                prediction = predict_price(price, sqft, bedrooms, bathrooms, offers, brick, neighborhood)

                # Display the prediction to the user
                st.write("Predicted price: ${:.2f}".format(prediction))
