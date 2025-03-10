# CSV File Editor

A simple web application for viewing and modifying CSV files with an intuitive interface.

![Screenshot from 2025-03-09 19-51-39](https://github.com/user-attachments/assets/2be7caa3-5dbd-4b1d-84a5-82b6ea186560)
![Screenshot from 2025-03-09 19-51-26](https://github.com/user-attachments/assets/b8404774-ae6d-4d69-8de0-c490fbb35a39)


## Features

- **Upload CSV File**: Easily upload your existing CSV files to the application
- **View CSV Data**: See your data displayed in a clean, tabular format
- **Add New Rows**: Quickly add new entries through a simple form interface
- **Modify Existing Data**: Edit any row with a user-friendly form
- **Delete Rows**: Remove unwanted data with a single click
- **Reset Session**: Start fresh or upload a different file whenever needed

## Installation

Follow these simple steps to get the application running on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/FathurRohmna/streamlit-table-editor-with-pandas.git
   cd streamlit-table-editor-with-pandas
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install streamlit pandas
   ```

3. **Launch the Application**:
   ```bash
   streamlit run main.py
   ```

4. **Access the App**:
   Open your browser and go to http://localhost:8501

## Usage

### Upload a CSV File
Click "Upload a CSV file" and select your file. Your data will immediately appear in a table.

### Add a New Row
1. Select "➕ Add Row" from the options
2. Fill in your data in the form fields
3. Click the "➕ Add Row" button to save

### Modify Existing Data
1. Select "✏️ Modify Existing Data"
2. Choose which row to edit from the dropdown
3. Update the information as needed
4. Click "✏️ Update Row" to save changes

### Delete a Row
1. Select "✏️ Modify Existing Data" 
2. Choose the row you want to remove
3. Click "🗑️ Delete" to remove it

### Reset Session
Click "♻️ Reset" anytime to clear your current work and start fresh.

## Example CSV Template

You can use the following template as a starting point for your CSV files:

```csv
id,name,email,phone,date_joined
1,John Doe,john.doe@example.com,555-123-4567,2023-01-15
2,Jane Smith,jane.smith@example.com,555-987-6543,2023-02-20
3,Robert Johnson,robert.j@example.com,555-456-7890,2023-03-05
```

Save this content to a file with a `.csv` extension (e.g., `contacts.csv`) and upload it to the application.

## Code Structure

- **main.py**: Core application with UI components and interactivity
- **lib/utils.py**: Helper functions for file handling
- **lib/csv_operations.py**: Class that manages all CSV manipulation operations

## Dependencies

- **Streamlit**: Powers the web interface
- **Pandas**: Handles the CSV data processing
