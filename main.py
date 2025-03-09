import streamlit as st
from lib.utils import upload_file
from lib.csv_operations import CSVOperations

def main():
    st.title("CSV File Editor")

    if "csv_ops" not in st.session_state:
        st.session_state.csv_ops = CSVOperations()
    if "success_message" not in st.session_state:
        st.session_state.success_message = None

    uploaded_file = upload_file()
    if uploaded_file is not None and not st.session_state.csv_ops.table_data:
        file_content = uploaded_file.getvalue().decode("utf-8").splitlines()
        st.session_state.csv_ops.load_csv(file_content)

    if st.session_state.csv_ops.table_data:
        df = st.session_state.csv_ops.get_dataframe()
        st.write("### Current Table")
        st.dataframe(df)

    st.write("### Add New Row")
    new_data = {}
    for col in st.session_state.csv_ops.columns:
        input_key = f"new_{col}"
        if input_key not in st.session_state:
            st.session_state[input_key] = ""
        new_data[col] = st.text_input(
            f"Enter {col}",
            value=st.session_state[input_key],
            key=input_key
        )

    if st.button("Add Row"):
        success, message = st.session_state.csv_ops.add_row(new_data)
        if success:
            st.session_state.success_message = message
            st.rerun()
        else:
            st.warning(message)

    if st.session_state.success_message:
        st.success(st.session_state.success_message)
        st.session_state.success_message = None

if __name__ == "__main__":
    main()