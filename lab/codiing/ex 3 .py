import numpy as np

# Input dataset
cricket_data = np.array([
    [3, 80, 2500],
    [6, 100, 4200],
    [4, 90, 3100],
    [8, 120, 5500],
    [10, 150, 7000]
])

# Select players with more than 4 centuries
selected_players = cricket_data[cricket_data[:, 0] > 4]

# Calculate average total runs
average_runs = np.mean(selected_players[:, 2])

print("Players with more than 4 centuries:")
print(selected_players)

print("\nAverage total runs:", average_runs)
