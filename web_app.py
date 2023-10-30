import streamlit as st

# Set page title and company logo
st.set_page_config(
    page_title="NexTurn AI Project",
    page_icon=":rocket:",
    layout="wide"
)

# Logo and title
st.image("Logo.png", width=100)
st.title("Welcome to NexTurn AI Project")

# Create tabs for cases
tabs = st.tabs(["Case 1", "Case 2", "Case 3"])

if tabs == "Case 1":
    st.write("Content for Case 1")

    st.markdown(
        """
        <div class="custom-container">
            <div class="case-content">
                <h3>Details for Case 1</h3>
                <p>This is the content for Case 1.</p>
            </div>
            <div class="case-link">
                <a href='https://your-case1-link.com' target='_blank'>Open Case 1</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif tabs == "Case 2":
    st.write("Content for Case 2")

    st.markdown(
        """
        <div class="custom-container">
            <div class="case-content">
                <h3>Details for Case 2</h3>
                <p>This is the content for Case 2.</p>
            </div>
            <div class="case-link">
                <a href='https://your-case2-link.com' target='_blank'>Open Case 2</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif tabs == "Case 3":
    st.write("Content for Case 3")

    st.markdown(
        """
        <div class="custom-container">
            <div class="case-content">
                <h3>Details for Case 3</h3>
                <p>This is the content for Case 3.</p>
            </div>
            <div class="case-link">
                <a href='https://your-case3-link.com' target='_blank'>Open Case 3</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Custom CSS to style the layout
st.markdown(
    """
    <style>
        .custom-container {
            display: flex;
            justify-content: space-between;
            margin: 20px;
            padding: 10px;
            border: 1px solid #ddd;
        }
        .case-content {
            flex: 2;
        }
        .case-link {
            flex: 1;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True
)
