import streamlit as st

def upload_file():
    st.sidebar.header("Upload Template")
    uploaded_file = st.sidebar.file_uploader("Select a CSV file to showing data", type=["csv"])
    return uploaded_file