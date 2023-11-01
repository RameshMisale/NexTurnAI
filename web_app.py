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
        "Case 1": {
            "content": "This is the content for Images Case 1.",
            "link": "https://www.example.com/images/case1"
        },
        "Case 2": {
            "content": "You can add content here for Images Case 2.",
            "link": "https://www.example.com/images/case2"
        },
        "Case 3": {
            "content": "You can add content here for Images Case 3.",
            "link": "https://www.example.com/images/case3"
        }
    },
    "Videos": {
        "Case 1": {
            "content": "This is the content for Videos Case 1.",
            "link": "https://www.example.com/videos/case1"
        },
        "Case 2": {
            "content": "You can add content here for Videos Case 2.",
            "link": "https://www.example.com/videos/case2"
        },
        "Case 3": {
            "content": "You can add content here for Videos Case 3.",
            "link": "https://www.example.com/videos/case3"
        }
    },
    "Audios": {
        "Case 1": {
            "content": "This is the content for Audios Case 1.",
            "link": "https://www.example.com/audios/case1"
        },
        "Case 2": {
            "content": "You can add content here for Audios Case 2.",
            "link": "https://www.example.com/audios/case2"
        },
        "Case 3": {
            "content": "You can add content here for Audios Case 3.",
            "link": "https://www.example.com/audios/case3"
        }
    }
}

# Display the selected tab's cases with links, subheaders, and content in container tabs
if selected_tab in cases:
    tab_content = cases[selected_tab]
    
    for case, case_data in tab_content.items():
        with st.container():
            st.subheader(case)
            st.write(case_data["content"])
            st.markdown(f"[Open {case}]({case_data['link']})", unsafe_allow_html=True)
