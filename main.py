from src.pipeline import Pipeline
import argparse

parser = argparse.ArgumentParser(description = "Run the sales data pipeline")

parser.add_argument(
    "--raw-file", 
    default="data/raw/sales.csv",
    help="Path to the raw input sales CSV file")

parser.add_argument(
    "--cleaned-file", 
    default="data/processed/cleaned_df.csv",
    help="Path where the cleaned sales CSV will be saved")

parser.add_argument(
    "--agg-country-file", 
    default="data/summary/agg_sales_by_country.csv",
    help="Path where the country summary CSV will be saved")

parser.add_argument(
    "--agg-category-file", 
    default="data/summary/agg_sales_by_category.csv",
    help="Path where the category summary CSV will be saved")

args = parser.parse_args()

'''
cleaned_df, summary_by_country, summary_by_category = pipeline.run_sales_pipeline(
    args.raw_file, 
    args.cleaned_file, 
    args.agg_country_file, 
    args.agg_category_file
)
'''

pipeline = Pipeline()

pipeline.run_sales_pipeline()