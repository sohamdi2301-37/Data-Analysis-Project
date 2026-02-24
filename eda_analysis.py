import pandas as pd

df = pd.read_csv("sales_data.csv")
df['invoice_date'] = pd.to_datetime(df['invoice_date'])

df['total_amount'] = df['quantity'] * df['price']

total_revenue = df['total_amount'].sum()
print("Total Revenue:", total_revenue)

category_sales = df.groupby('product_category')['total_amount'].sum()
print("\nRevenue by Category:")
print(category_sales)

customer_sales = df.groupby('customer_id')['total_amount'].sum()
print("\nCustomer Revenue:")
print(customer_sales)

monthly_sales = df.resample('M', on='invoice_date')['total_amount'].sum()
print("\nMonthly Sales:")
print(monthly_sales)
