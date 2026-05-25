from src.extract import Extract
from src.transform import Transform
from src.load import Load
import logging

logging.basicConfig(level = logging.INFO)

class Pipeline:
    def __init__(self):
        self.extractor = Extract()
        self.transformer = Transform()
        self.loader = Load()

    def run_sales_pipeline(self, raw_file_path, processed_file_path, summary_by_country_file_path, summary_by_category_file_path):
        
        logging.info(f"Reading raw sales data from {raw_file_path}")

        data = self.extractor.extract_sales_csv(raw_file_path)
        logging.info("Raw rows: %s", len(data))

        cleaned_df = self.transformer.clean_sales_data(data)

        logging.info("Cleaned dataframe with %s", len(cleaned_df))
        logging.info("Total rows removed from raw file %s", len(data) - len(cleaned_df))

        summary_by_country = self.transformer.summarize_sales_by_country(cleaned_df)
        summary_by_category = self.transformer.summarize_sales_by_category(cleaned_df)
        
        self.loader.save_as_csv(cleaned_df, processed_file_path)
        logging.info(f"Saved claned dataframe to {processed_file_path}")

        self.loader.save_as_csv(summary_by_country, summary_by_country_file_path)
        logging.info(f"Saved summarized data by country to {summary_by_country_file_path}")

        self.loader.save_as_csv(summary_by_category, summary_by_category_file_path)
        logging.info(f"Saved summarized data by category to {summary_by_category_file_path}")

        return cleaned_df, summary_by_country, summary_by_category
