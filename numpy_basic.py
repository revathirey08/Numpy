import numpy as np

marks = np.array([80, 75, 90, 85, 95])

print("Original Array:", marks)

print("Dimensions:", marks.ndim)

print("Size:", marks.size)


print("Data Type:", marks.dtype)


print("Shape:", marks.shape)


print("First Mark:", marks[0])
print("Third Mark:", marks[2])
print("Last Mark:", marks[-1])

print("First Three Marks:", marks[0:3])

print("Add 5:", marks + 5)


print("Subtract 5:", marks - 5)


print("Multiply by 2:", marks * 2)


print("Divide by 5:", marks / 5)


print("Total:", np.sum(marks))


print("Average:", np.mean(marks))


print("Highest Mark:", np.max(marks))


print("Lowest Mark:", np.min(marks))


print("Sorted Marks:", np.sort(marks))

zeros = np.zeros(5)
print("Zero Array:", zeros)


ones = np.ones(5)
print("One Array:", ones)


numbers = np.arange(1, 11)
print("Number Sequence:", numbers)