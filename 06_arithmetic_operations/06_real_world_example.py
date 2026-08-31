import numpy as np

# Product prices
prices = np.array([500, 1000, 750, 1200, 2000])

# Quantity sold
quantity = np.array([2, 3, 5, 2, 1])

print("Product Prices:")
print(prices)

print("\nQuantity Sold:")
print(quantity)

# Calculate total sales for each product
sales = prices * quantity

print("\nTotal Sales per Product:")
print(sales)

# Apply 10% discount
discount = sales * 0.10

print("\nDiscount:")
print(discount)

# Final sales after discount
final_sales = sales - discount

print("\nFinal Sales:")
print(final_sales)

# # Total Revenue
# total_revenue = np.sum(final_sales)

# print("\nTotal Revenue:", total_revenue)

# Product Prices:
# [ 500 1000  750 1200 2000]

# Quantity Sold:
# [2 3 5 2 1]

# Total Sales per Product:
# [1000 3000 3750 2400 2000]

# Discount:
# [100. 300. 375. 240. 200.]

# Final Sales:
# [ 900. 2700. 3375. 2160. 1800.]

# Total Revenue: 10935.0