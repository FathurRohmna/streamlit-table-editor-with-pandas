import streamlit as st
from lib.utils import upload_file
from lib.csv_operations import CSVOperations

def reset_session():
    st.session_state.csv_ops = CSVOperations()
    st.session_state.success_message = None
    st.session_state.reset_form = False
    st.session_state.uploaded_file = None

def main():
    st.title("CSV File Editor")

    if "csv_ops" not in st.session_state:
        reset_session()
    
    if st.session_state.uploaded_file is None:
        uploaded_file = upload_file()
        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
            file_content = uploaded_file.getvalue().decode("utf-8").splitlines()
            st.session_state.csv_ops.load_csv(file_content)
            st.rerun()
    else:
        col1, col2 = st.columns([5, 1])
        with col1:
            st.write(f"Uploaded file: **{st.session_state.uploaded_file.name}**")
        with col2:
            if st.button("♻️ Reset", key="reset_button"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        
    if len(st.session_state.csv_ops.table_data) > 0 and st.session_state.uploaded_file is not None:
        df = st.session_state.csv_ops.get_dataframe()
        st.write("### Current Table")
        st.dataframe(df)

        st.write("➕ Add New Row")
        new_data = {}
        for col in st.session_state.csv_ops.columns:
            input_key = f"new_{col}"
            if st.session_state.reset_form:
                new_data[col] = st.text_input(f"Enter {col}", value="", key=input_key)
            else:
                if input_key not in st.session_state:
                    st.session_state[input_key] = ""
                new_data[col] = st.text_input(
                    f"Enter {col}",
                    value=st.session_state[input_key],
                    key=input_key
                )

        col = st.columns(1)[0]

        with col:
            if st.button("➕ Add Row", use_container_width=True, key="add_button"):
                success, message = st.session_state.csv_ops.add_row(new_data)
                if success:
                    st.session_state.success_message = message
                    st.session_state.reset_form = True
                    st.rerun()
                else:
                    st.warning(message)
        
        if st.session_state.success_message:
            st.success(st.session_state.success_message)
            st.session_state.success_message = None
            st.session_state.reset_form = False

        st.write("✏️ Modify Existing Data")
        row_options = [
            f"Row {idx + 1}: {list(row.values())}"
            for idx, row in enumerate(st.session_state.csv_ops.table_data)
        ]
        selected_index = st.selectbox(
            "Select a row to modify", 
            options=list(range(len(st.session_state.csv_ops.table_data))), 
            format_func=lambda x: row_options[x], 
            key="index_modify"
        )
        selected_row = st.session_state.csv_ops.table_data[selected_index]

        edit_data = {}
        for col in st.session_state.csv_ops.columns:
            edit_data[col] = st.text_input(
                f"Edit {col}",
                selected_row[col],
                key=f"edit_{col}_{selected_index}"
            )

        col1, col2 = st.columns([5, 1])
        with col1:
            if st.button("✏️ Update Row", key="update_button"):
                success, message = st.session_state.csv_ops.update_row(selected_index, edit_data)
                if success:
                    st.session_state.success_message = message
                    st.rerun()
                else:
                    st.warning(message)
                
        with col2:
            if st.button("🗑️ Delete", key="delete_button"): 
                success, message = st.session_state.csv_ops.delete_row(selected_index)
                if success:
                    st.session_state.success_message = message
                    st.rerun()
                else:
                    st.warning(message)
            
    elif len(st.session_state.csv_ops.table_data) == 0 and st.session_state.uploaded_file is not None:
        st.error("File is empty")

    else:
        st.warning("Select a CSV file to edit data")

if __name__ == "__main__":
    main()
