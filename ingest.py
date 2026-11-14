import duckdb

con = duckdb.connect("ecommerce.duckdb")
con.execute("CREATE SCHEMA IF NOT EXISTS raw;")

con.execute("""
CREATE or REPLACE TABLE raw.orders AS
SELECT * FROM read_csv_auto('raw_data/olist_orders_dataset.csv');
""")

con.execute("""
CREATE or REPLACE TABLE raw.customers AS
SELECT * FROM read_csv_auto('raw_data/olist_customers_dataset.csv');
""")

con.execute("""
CREATE or REPLACE TABLE raw.order_items AS
SELECT * FROM read_csv_auto('raw_data/olist_order_items_dataset.csv');
""")

print("SUCCESS: Raw tables loaded into ecommerce.duckdb!")

con.close()