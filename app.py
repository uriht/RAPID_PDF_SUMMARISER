import streamlit as st
from txtai.pipeline import Summary
from PyPDF2 import PdfReader

# Set page layout to wide
st.set_page_config(layout="wide")

# Define a function to apply custom CSS styles
def set_custom_style():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f0f0;
        }
        .st-bd {
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to summarize text
@st.cache_data
def text_summary(text, maxlength=None):
    summary = Summary()
    result = summary(text)
    return result

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

# Add a title and description with emoji
st.title("📄 Text Summarization App 📝")
st.markdown("This app allows you to summarize text or documents. 🚀")

# Create a sidebar to select the operation
choice = st.sidebar.selectbox("Select your choice", ["Summarize Text", "Summarize Document"])

# Set a custom style
set_custom_style()

# Main content based on user choice
if choice == "Summarize Text":
    st.subheader("Summarize Text using txtai")
    input_text = st.text_area("Enter your text here", height=200)
    if st.button("Summarize Text 📑"):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("📄 **Your Input Text**")
            st.info(input_text)
        with col2:
            st.markdown("📝 **Summary Result**")
            result = text_summary(input_text)
            st.success(result)

elif choice == "Summarize Document":
    st.subheader("Summarize Document using txtai")
    input_file = st.file_uploader("Upload your document here (PDF) 📂", type=['pdf'])
    if input_file is not None:
        if st.button("Summarize Document 📑"):
            with open("doc_file.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1, 1])
            with col1:
                st.info("File uploaded successfully 📤")
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("📜 **Extracted Text is Below:**")
                st.info(extracted_text)
            with col2:
                st.markdown("📝 **Summary Result**")
                doc_summary = text_summary(extracted_text)
                st.success(doc_summary)
