import pandas as pd

# Load the original Excel file
df = pd.read_csv('Hotel_sales_clean.csv')

print("Original shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())