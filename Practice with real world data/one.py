# Data Structure: [restaurant_id, 2021, 2022, 2023, 2024]

import numpy as np


sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],   # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],   # Beijing Bites
    [3, 200000, 230000, 260000, 300000],   # Pizza Hub
    [4, 180000, 210000, 240000, 270000],   # Burger Point
    [5, 160000, 185000, 205000, 230000]    # Food king
])

print("===== Zomato Sales Analysis =====")
print("\n Sales data shape", sales_data.shape)

print("\n Sample data for 1st three restaurant: ", sales_data[:3])
print("\n Sample data for 1st three restaurant: ", sales_data[:, 1:])


# total sales per year

print(np.sum(sales_data, axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0)   # axis=0 (columns)
print(yearly_total)


# Minimum sales per restaurant

min_sales = np.min(sales_data[:, 1:], axis=1)   # axis=1 (rows)
print(min_sales)


# Minimum sales per year

max_sales = np.max(sales_data[:, 1:], axis=0)
print(max_sales)



# Average sales per restaurant

avg_sales = np.mean(sales_data[:, 1:], axis=1)
print(avg_sales)



# Cumulative Sum

cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print(cumsum)
# [150000 330000 550000 800000]
#  [120000 260000 420000 610000]
#  [200000 430000 690000 990000]
#  [180000 390000 630000 900000]
#  [160000 345000 550000 780000]]

