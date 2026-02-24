# Python Fundamentals Example

store_name = "Retail Store"
total_sales = 50000
gst_rate = 18

gst_amount = total_sales * gst_rate / 100
final_amount = total_sales + gst_amount

print("Store Name:", store_name)
print("GST Amount:", gst_amount)
print("Final Amount:", final_amount)

categories = ["Electronics", "Clothing", "Grocery"]

for category in categories:
    print("Product Category:", category)

def calculate_total(quantity, price):
    return quantity * price

print("Sample Calculation:", calculate_total(2, 15000))
