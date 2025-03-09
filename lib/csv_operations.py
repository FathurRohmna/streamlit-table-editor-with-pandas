import csv
import pandas as pd

class CSVOperations:
    def __init__(self, file_content=None):
        self.table_data = []
        self.columns = []
        if file_content:
            self.load_csv(file_content)

    def load_csv(self, file_content):
        self.table_data = list(csv.DictReader(file_content))
        self.columns = self.table_data[0].keys() if self.table_data else []

    def get_dataframe(self):
        return pd.DataFrame(self.table_data)

    def add_row(self, new_data):
        if all(new_data.values()): 
            self.table_data.append(new_data)
            return True, "Row added successfully!"
        else:
            return False, "Please fill all fields before adding."
        
    def update_row(self, index, updated_data):
        if 0 <= index < len(self.table_data):
            self.table_data[index] = updated_data
            return True, "Row updated successfully!"
        else:
            return False, "Invalid row index."

    def delete_row(self, index):
        if 0 <= index < len(self.table_data):
            self.table_data.pop(index)
            return True, "Row deleted successfully!"
        else:
            return False, "Invalid row index."
    