import numpy as np

# Input dataset
cricket_products = np.array([
    [2500, 3000, 2800],
    [1200, 1500, 1300],
    [800, 1000, 900]
])

# Calculate average price of all products
average_price = np.mean(cricket_products)

print("Average price of cricket products:", average_price)
