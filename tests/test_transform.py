from src.transform import Transform
import pandas as pd

def test_clean_sales_data_removes_invalid_rows():
    
    test_data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "order_date": ["2026-01-01", "bad_date", "2026-01-03"],
            "customer_id": ["C001", "C002", "C003"],
            "product": [" Laptop ", "Mouse", "Keyboard"],
            "category": ["electronics", "Electronics", "ELECTRONICS"],
            "quantity": [2, 1, "two"],
            "unit_price": [100.0, 50.0, 20.0],
            "country": ["USA", "USA", None],
        }
    )

    transformer = Transform()

    cleaned_df = transformer.clean_sales_data(test_data)

    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]["product"] == "Laptop"
    assert cleaned_df.iloc[0]["category"] == "Electronics"
    assert cleaned_df.iloc[0]["quantity"] == 2
    assert cleaned_df.iloc[0]["total_sale"] == 200.0

def test_summarize_sales_by_category():
    test_data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "category": ["Electronics", "Electronics", "Furniture"],
            "total_sale": [100.0, 200.0, 50.0],
        }
    )

    transformer = Transform()

    summary = transformer.summarize_sales_by_category(test_data)

    electronics = summary.query("category == 'Electronics'")

    assert electronics.iloc[0]["total_amount"] == 300.0

def test_summary_sales_by_country():
    
    test_data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "country": ["Brazil", "USA", "USA"],
            "total_sale": [100.0, 200.0, 50.0]
        }
    )

    transformer = Transform()

    summary = transformer.summarize_sales_by_country(test_data)

    usa_data = summary.query("country == 'USA'")

    assert usa_data["total_amount"].sum() == 250.0

def test_check_required_columns():

    required_columns = ["quantity", "unit_price", "order_date", "category", "product", "country"]

    transformer = Transform()

    test_data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "order_date": ["2026-01-01", "bad_date", "2026-01-03"],
            "customer_id": ["C001", "C002", "C003"],
            "product": [" Laptop ", "Mouse", "Keyboard"],
            "category": ["electronics", "Electronics", "ELECTRONICS"],
            "quantity": [2, 1, "two"],
            "unit_price": [100.0, 50.0, 20.0],
            "country": ["USA", "USA", None],
        }
    )

    missing_columns = transformer.check_required_columns(test_data, required_columns)
    
    assert missing_columns == []