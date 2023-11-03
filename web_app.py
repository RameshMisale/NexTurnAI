import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

st.image("Logo.png", width=400, use_column_width=False)
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs1, tabs2, tabs3 = st.tabs(["General", "Text", "Images"])

# House Price Prediction Section
with tabs1:
    st.write("House Price Prediction (Regression)")
    
    # Create input fields for user input
    st.sidebar.title('Input Features')
    age = st.sidebar.number_input("Age")
    sqft = st.sidebar.number_input("SqFt")
    bedrooms = st.sidebar.number_input("Bedrooms")
    bathrooms = st.sidebar.number_input("Bathrooms")
    offers = st.sidebar.number_input("Offers")
    brick = st.sidebar.checkbox("Brick")

    # Load the pre-trained regression model using pickle
    with open('Regression_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Age': [age],
        'SqFt': [sqft],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Offers': [offers],
        'Brick': [int(brick)]
    })

    if st.sidebar.button("Predict House Price"):
        # Make the prediction
        predicted_price = model.predict(input_data)[0]
        st.write(f"Predicted House Price: ${predicted_price:,.2f}")

# Cancer Prediction Section
with tabs2:
    st.write("Cancer Prediction (Classification)")
    
    # Create input fields for user input
    st.sidebar.title('Input Features')
    age = st.sidebar.number_input("Age")
    bmi = st.sidebar.number_input("BMI")
    glucose = st.sidebar.number_input("Glucose")
    insulin = st.sidebar.number_input("Insulin")
    homa = st.sidebar.number_input("HOMA")
    leptin = st.sidebar.number_input("Leptin")
    adiponectin = st.sidebar.number_input("Adiponectin")
    resistin = st.sidebar.number_input("Resistin")
    mcp1 = st.sidebar.number_input("MCP.1")

    # Load the pre-trained classification model using pickle
    with open('Classification_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Age': [age],
        'BMI': [bmi],
        'Glucose': [glucose],
        'Insulin': [insulin],
        'HOMA': [homa],
        'Leptin': [leptin],
        'Adiponectin': [adiponectin],
        'Resistin': [resistin],
        'MCP.1': [mcp1]
    })

    if st.sidebar.button("Predict Cancer"):
        # Make the prediction
        predicted_class = model.predict(input_data)[0]
        st.write(f"Predicted Cancer Class: {predicted_class}")

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
