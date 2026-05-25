import pandas as pd

class Extract:
    def extract_sales_csv(self, path):
        df = pd.read_csv(path)
        return df