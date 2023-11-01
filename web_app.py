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

# Display the selected tab's cases with links, subheaders, and content side by side
if selected_tab in cases:
    tab_content = cases[selected_tab]
    
    col1, col2 = st.columns(2)
    
    for case in tab_content:
        with col1:
            st.subheader(case)
            st.write(tab_content[case]["content"])
            st.markdown(f"[Open {case}]({tab_content[case]['link']})", unsafe_allow_html=True)
            
    # If there's a next case, display it in the second column
    next_case = list(tab_content.keys())[1:]
    if next_case:
        with col2:
            st.subheader(next_case[0])
            st.write(tab_content[next_case[0]]["content"])
            st.markdown(f"[Open {next_case[0]}]({tab_content[next_case[0]]['link']})", unsafe_allow_html=True)
