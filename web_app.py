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
tabs1, tabs2, tabs3 = st.tabs(["General", "Text", "Images"])
with tabs1:
    st.write("Content for image Cases")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Case 1")
        st.write("House Price Prediction")
        #if st.button("Open House Price Prediction"):
        st.markdown("[Open House Price Prediction](https://appgui-jk6qksscd9ckag6lmcemz9.streamlit.app/)", unsafe_allow_html=True)


    # Rest of your code...


    with col2:
        st.subheader("Case 2")
        st.write("Add the content for Case 2.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

    with col3:
        st.subheader("Case 3")
        st.write("Add the content for Case 3.")
        st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

with tabs2:
    st.write("Content is under construction...")
    st.write("!!!...COMING SOON..!!!")
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.subheader("Case 1")
    #     st.write("Add content for Case 1.")
    #     st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    # with col2:
    #     st.subheader("Case 2")
    #     st.write("Add content for Case 2.")
    #     st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    # with col3:
    #     st.subheader("Case 3")
    #     st.write("Add content for Case 3.")
    #     st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

with tabs3:
    st.write("Content is under construction...")
    st.write("!!!...COMING SOON..!!!")
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.subheader("Case 1")
    #     st.write("Add content for Case 1.")
    #     st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    # with col2:
    #     st.subheader("Case 2")
    #     st.write("Add content for Case 2.")
    #     st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)
    # with col3:
    #     st.subheader("Case 3")
    #     st.write("Add content for Case 3.")
    #     st.markdown("[Open in a new browser](https://www.example.com)", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Thank you for visiting...!!")
