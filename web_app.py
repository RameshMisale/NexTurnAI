import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.columns(3)

with tab1:
    if st.button("Tab 1"):
        st.header("Tab 1 Content")
        st.write("This is the content for Tab 1.")
        st.image("image1.jpg", use_column_width=True)

with tab2:
    if st.button("Tab 2"):
        st.header("Tab 2 Content")
        st.write("This is the content for Tab 2.")
        st.write("You can add more elements here.")
        st.image("image2.jpg", use_column_width=True)

with tab3:
    if st.button("Tab 3"):
        st.header("Tab 3 Content")
        st.write("This is the content for Tab 3.")
        st.write("You can add more elements here.")
        st.image("image3.jpg", use_column_width=True)
