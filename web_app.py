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

# Create tabs for different sections
tabs = st.tabs(["General Case 1", "General Case 2"])

# General Case 1: House Price Prediction Section
with tabs[0]:
    st.write("General Case 1: House Price Prediction (Regression)")
    st.sidebar.title('Input Features')
    age = st.sidebar.number_input("Age")
    sqft = st.sidebar.number_input("SqFt")
    bedrooms = st.sidebar.number_input("Bedrooms")
    bathrooms = st.sidebar.number_input("Bathrooms")
    offers = st.sidebar.number_input("Offers")
    brick = st.sidebar.checkbox("Brick")

    with open('Regression_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    input_data = pd.DataFrame({
        'Age': [age],
        'SqFt': [sqft],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Offers': [offers],
        'Brick': [int(brick)]
    })

    if st.sidebar.button("Predict House Price"):
        predicted_price = model.predict(input_data)[0]
        st.write(f"Predicted House Price: ${predicted_price:,.2f}")

# General Case 2: Cancer Prediction Section
with tabs[1]:
    st.write("General Case 2: Cancer Prediction (Classification)")
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

    with open('Classification_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

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
        predicted_class = model.predict(input_data)[0]
        st.write(f"Predicted Cancer Class: {predicted_class}")

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
