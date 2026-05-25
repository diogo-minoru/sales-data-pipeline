from src.pipeline import Pipeline

pipeline = Pipeline()

cleaned_df, summary_by_country, summary_by_category = pipeline.run_sales_pipeline("data/raw/sales.csv", "data/processed/cleaned_df.csv", "data/summary/agg_sales_by_country.csv", "data/summary/agg_sales_by_category.csv")