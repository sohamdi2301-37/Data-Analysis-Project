import pandas as pd

df = pd.read_csv("sales_data_extended.csv")

# Frequency calculation
frequency = df.groupby('customer_id')['invoice_id'].count()

print("Customer Purchase Frequency:")
print(frequency)
