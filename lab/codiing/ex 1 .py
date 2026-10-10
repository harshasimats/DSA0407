import numpy as np

# Input dataset
student_scores = np.array([
    [65, 82, 110, 45],
    [72, 95, 125, 52],
    [58, 78, 98, 40],
    [85, 105, 135, 60]
])

formats = ["T20", "ODI", "Test", "T10"]

# Calculate average score for each format
average_scores = np.mean(student_scores, axis=0)

print("Average score for each cricket format:")
for i in range(len(formats)):
    print(formats[i], ":", average_scores[i])

# Find format with highest average
highest_index = np.argmax(average_scores)
print("\nFormat with highest average:", formats[highest_index])
