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
    