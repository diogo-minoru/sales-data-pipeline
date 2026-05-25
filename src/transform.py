import pandas as pd

class Transform:

    def check_required_columns(self, data, required_columns):
        missing_columns = []

        for column in required_columns:
            if column not in data.columns:
                missing_columns.append(column)
        
        return missing_columns

    def clean_sales_data(self, data):

        required_columns = ["quantity", "unit_price", "order_date", "category", "product", "country"]

        missing_columns = self.check_required_columns(data, required_columns)

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        data = data.copy()
        
        data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")
        data["unit_price"] = pd.to_numeric(data["unit_price"], errors="coerce")
        data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce", format="mixed")
        data["product"] = data["product"].str.strip()
        data["category"] = data["category"].str.strip().str.capitalize()
        
        # data["country"] = np.where(data["country"].isnull(), "Unknown", data["country"])
        data["country"] = data["country"].fillna("Unknown").str.strip()

        data = data.dropna(subset = ["quantity", "unit_price", "order_date"])

        data = data.query("quantity > 0") # [data["quantity"] > 0]
        data = data.query("unit_price > 0") #[data["unit_price"] > 0]

        data["quantity"] = data["quantity"].astype("int64")

        data["total_sale"] = data["quantity"] * data["unit_price"]

        return data

    def summarize_sales_by_category(self, data):
        
        # summarized_by_category = summarized_by_category.groupby("category")["total_sale"].sum()
        
        summarized_by_category = data.groupby("category").agg(
            total_amount = ("total_sale", "sum"),
            total_transactions = ("order_id", "nunique")
        ).reset_index()
        
        summarized_by_category["avg_ticket"] = summarized_by_category["total_amount"] / summarized_by_category["total_transactions"]
        
        return summarized_by_category
    
    def summarize_sales_by_country(self, data):
        
        summarized_by_country = data.groupby("country").agg(
            total_amount = ("total_sale", "sum"),
            total_transactions = ("order_id", "nunique")
        ).reset_index()

        summarized_by_country["avg_ticket"] = summarized_by_country["total_amount"] / summarized_by_country["total_transactions"]
        
        return summarized_by_country