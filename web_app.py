import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo and title with an increased size
st.image("Logo.png", width=400, use_column_width=False)  # Adjust the width value
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs = ["Images", "Videos", "Audios"]
selected_tab = st.radio("Select a case type:", tabs)

# Define the content for each case in a dictionary with different links
cases = {
    "Images": {
        "Case 1": "This is the content for Images Case 1.",
        "Case 2": "You can add content here for Images Case 2.",
        "Case 3": "You can add content here for Images Case 3."
    },
    "Videos": {
        "Case 1": "This is the content for Videos Case 1.",
        "Case 2": "You can add content here for Videos Case 2.",
        "Case 3": "You can add content here for Videos Case 3."
    },
    "Audios": {
        "Case 1": "This is the content for Audios Case 1.",
        "Case 2": "You can add content here for Audios Case 2.",
        "Case 3": "You can add content here for Audios Case 3."
    }
}

# Define links for each case type
links = {
    "Images": {
        "Case 1": "https://www.example.com/images/case1",
        "Case 2": "https://www.example.com/images/case2",
        "Case 3": "https://www.example.com/images/case3"
    },
    "Videos": {
        "Case 1": "https://www.example.com/videos/case1",
        "Case 2": "https://www.example.com/videos/case2",
        "Case 3": "https://www.example.com/videos/case3"
    },
    "Audios": {
        "Case 1": "https://www.example.com/audios/case1",
        "Case 2": "https://www.example.com/audios/case2",
        "Case 3": "https://www.example.com/audios/case3"
    }
}

# Display the selected tab's cases with links in side-by-side columns
if selected_tab in cases:
    tab_content = cases[selected_tab]
    tab_links = links[selected_tab]
    col1, col2, col3 = st.columns(3)
    for case, content in tab_content.items():
        st.subheader(case)
        col = col1 if case == "Case 1" else (col2 if case == "Case 2" else col3)
        with col:
            st.write(content)
            st.markdown(f"[Open {case}]({tab_links[case]})", unsafe_allow_html=True)
