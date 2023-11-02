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
tabs1, tabs2, tabs3 = st.columns(3)

with tabs1:
    st.subheader("Case 1")
    st.write("Click the button to open the House Price Prediction GUI")
    if st.button("Open House Price Prediction"):
        # Redirect to the House Price Prediction page using query parameters
        st.experimental_set_query_params(page="house_price_prediction")

with tabs2:
    st.subheader("Case 2")
    st.write("Add the content for Case 2.")

with tabs3:
    st.subheader("Case 3")
    st.write("Add the content for Case 3.")

# Check if the query parameter "page" is set to "house_price_prediction"
if "page" in st.experimental_get_query_params() and st.experimental_get_query_params()["page"] == "house_price_prediction.py":
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
