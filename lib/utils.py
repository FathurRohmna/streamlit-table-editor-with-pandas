import streamlit as st

def upload_file():
    uploaded_file = st.file_uploader("Select a CSV file to edit data", type=["csv"])
    return uploaded_file