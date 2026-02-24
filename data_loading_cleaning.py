import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Original Data:")
print(df.head())

df['invoice_date'] = pd.to_datetime(df['invoice_date'])

df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

print("\nCleaned Data Info:")
print(df.info())
