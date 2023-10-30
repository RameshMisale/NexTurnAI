import streamlit as st

# Create tabs using st.radio
selected_tab = st.radio("Select a tab:", ["Tab 1", "Tab 2", "Tab 3"])

# Content for Tab 1
if selected_tab == "Tab 1":
    st.header("Tab 1 Content")
    st.write("This is the content for Tab 1.")
    st.image("image1.jpg", use_column_width=True)

# Content for Tab 2
elif selected_tab == "Tab 2":
    st.header("Tab 2 Content")
    st.write("This is the content for Tab 2.")
    st.write("You can add more elements here.")
    st.image("image2.jpg", use_column_width=True)

# Content for Tab 3
elif selected_tab == "Tab 3":
    st.header("Tab 3 Content")
    st.write("This is the content for Tab 3.")
    st.write("You can add more elements here.")
    st.image("image3.jpg", use_column_width=True)
