import streamlit as st
from lib.utils import upload_file
from lib.csv_operations import CSVOperations

def main():
    st.title("CSV File Editor")

    if "csv_ops" not in st.session_state:
        st.session_state.csv_ops = CSVOperations()

    uploaded_file = upload_file()
    if uploaded_file is not None and not st.session_state.csv_ops.table_data:
        file_content = uploaded_file.getvalue().decode("utf-8").splitlines()
        st.session_state.csv_ops.load_csv(file_content)

    if st.session_state.csv_ops.table_data:
        df = st.session_state.csv_ops.get_dataframe()
        st.write("### Current Table")
        st.dataframe(df)

if __name__ == "__main__":
    main()