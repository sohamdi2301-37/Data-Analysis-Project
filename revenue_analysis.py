import pandas as pd

df = pd.read_csv("sales_data_extended.csv")
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
df['total_amount'] = df['quantity'] * df['price']

# Revenue by Category
category_revenue = df.groupby('product_category')['total_amount'].sum()
print("Revenue by Category:")
print(category_revenue)

# Revenue by Customer
customer_revenue = df.groupby('customer_id')['total_amount'].sum()
print("\nRevenue by Customer:")
print(customer_revenue)
