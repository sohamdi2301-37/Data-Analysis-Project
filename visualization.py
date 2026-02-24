import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
df['total_amount'] = df['quantity'] * df['price']

category_sales = df.groupby('product_category')['total_amount'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

monthly_sales = df.resample('M', on='invoice_date')['total_amount'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
