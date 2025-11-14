import pandas as pd
# Load the data
df = pd.read_csv("../data/sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# ACCURACY - Check for impossible values
print("Accuracy Check")
negative_prices = (df["price"] < 0).sum()
current_date = pd.Timestamp.now()
future_dates_count = (df["date"] > current_date).sum()
print(f"Negative Prices: {negative_prices}")
print(f"Number of Future Dates: {future_dates_count}")
print()

# CONSISTENCY - Check standardization
print("Consistency Check")
unique_products = df["product"].unique()
unique_count = df["product"].nunique()
print("Unique products:", unique_products)
print("Count of unique products:", unique_count)
print()

# COMPLETENESS - Missing values
print("Completeness Check")
missing_values = df.isnull().sum()
completeness = df.notnull().mean().mean() * 100
print(f"Missing Values: {missing_values}")
print(f"Overall completeness rate: {completeness:.1f}%")

assert(df["price"] >= 0).all(), "Found Negative prices"