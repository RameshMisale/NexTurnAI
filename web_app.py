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
        st.write("Add the content for Case 1.")
        
        # ML Model Integration
        st.subheader("ML Model Prediction")
        user_input = st.text_input("Enter data for prediction:")
        if st.button("Get Prediction"):
            # Load your pre-trained ML model
            model = joblib.load('Regression_model.pkl')
            
            # Make predictions
            prediction = model.predict([user_input])
            st.write(f"Prediction: {prediction}")

        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

    with col2:
        st.subheader("Case 2")
        st.write("Add the content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

    with col3:
        st.subheader("Case 3")
        st.write("Add the content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

with tabs2:
    # Similar structure as tabs1 for Videos
    st.write("Content for Video Cases")
    # ...
    # (Repeat the structure for other tabs)
 
with tabs3:
    # Similar structure as tabs1 for Audios
    st.write("Content for Audio Cases")
    # ...
    # (Repeat the structure for other tabs)

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
