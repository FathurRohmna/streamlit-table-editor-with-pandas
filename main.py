import streamlit as st
from utils import upload_file

def main():
    st.title("CRUD Application with Streamlit and Pandas")
    
    uploaded_file = upload_file()

if __name__ == "__main__":
    main()