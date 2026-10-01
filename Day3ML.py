import numpy as np


marks = np.array([60, 70, 80, 90, 100])


mean = np.mean(marks)
print("Mean:", mean)


median = np.median(marks)
print("Median:", median)

variance = np.var(marks)
print("Variance:", variance)

std = np.std(marks)
print("Standard Deviation:", std)

passed = np.sum(marks >= 50)
total = len(marks)

probability = passed / total
print("Pass Probability:", probability)


study_hours = np.array([2, 3, 4, 5, 6])

correlation = np.corrcoef(study_hours, marks)[0, 1]
print("Correlation:", correlation)


covariance = np.cov(study_hours, marks)[0, 1]
print("Covariance:", covariance)


vector = np.array([2, 4, 6])
print("Vector:", vector)

matrix = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix:")
print(matrix)

result = np.dot(matrix, matrix)

print("Matrix Multiplication:")
print(result)