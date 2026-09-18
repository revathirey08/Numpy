import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Array A:", a)
print("Array B:", b)

print("Add:", np.add(a, b))


print("Subtract:", np.subtract(a, b))


print("Multiply:", np.multiply(a, b))


print("Divide:", np.divide(a, b))


print("Square Root:", np.sqrt(a))


print("Power:", np.power(a, 2))

c = np.array([-10, -20, 30, -40])
print("Absolute:", np.absolute(c))


print("Exponential:", np.exp(a))


print("Logarithm:", np.log(a))

import numpy as np


marks = np.array([60, 70, 80, 90, 100])

print("Marks:", marks)

print("Sum:", np.sum(marks))


print("Minimum:", np.min(marks))


print("Maximum:", np.max(marks))


print("Mean:", np.mean(marks))


print("Median:", np.median(marks))


print("Standard Deviation:", np.std(marks))

print("Variance:", np.var(marks))


print("Average:", np.average(marks))


print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))