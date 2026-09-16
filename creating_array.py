import numpy as np


a = np.empty(5)
print("Empty Array:", a)


b = np.full(5, 10)
print("Full Array:", b)


c = np.linspace(0, 10, 5)
print("Linspace:", c)


d = np.eye(3)
print("Eye Matrix:")
print(d)


e = np.identity(3)
print("Identity Matrix:")
print(e)


f = np.random.rand(5)
print("Random Numbers:", f)


g = np.random.randint(1, 11, 5)
print("Random Integers:", g)

import numpy as np

# Create a 2D NumPy Array
marks = np.array([
    [80, 75, 90],
    [85, 95, 88]
])

print("Marks:")
print(marks)


print("Dimensions:", marks.ndim)


print("Shape:", marks.shape)


print("Size:", marks.size)


print("Data Type:", marks.dtype)


print("Item Size:", marks.itemsize)

print("Total Bytes:", marks.nbytes)