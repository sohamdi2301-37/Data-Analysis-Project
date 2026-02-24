import pandas as pd

df = pd.read_csv("sales_data_extended.csv")
df['invoice_date'] = pd.to_datetime(df['invoice_date'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create total amount
df['total_amount'] = df['quantity'] * df['price']

# Remove negative or zero values
df = df[df['quantity'] > 0]
df = df[df['price'] > 0]

print("Cleaned Data:")
print(df.head())
