from src.extract import Extract
from src.transform import Transform
from src.load import Load

extractor = Extract()
transform = Transform()
load = Load()

df = extractor.extract_sales_csv('data/raw/sales.csv')
cleaned_df = transform.clean_sales_data(df)
load.save_as_csv(cleaned_df, "data/processed/cleaned_df.csv")

sales_by_category = transform.summarize_sales_by_category(cleaned_df)
load.save_as_csv(sales_by_category, "data/summary/agg_sales_by_category.csv")

sales_by_country = transform.summarize_sales_by_country(cleaned_df)
load.save_as_csv(sales_by_country, "data/summary/agg_sales_by_country.csv")

print(cleaned_df)
print(sales_by_country)
print(sales_by_category)

# load.save_as_csv(cleaned_df, "data/processed/processed_sales.csv")