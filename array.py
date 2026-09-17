import numpy as np

marks = np.array([80, 75, 90, 85, 95])

print("1D Array:")
print(marks)

print("First element:", marks[0])
print("Third element:", marks[2])
print("Last element:", marks[-1])



students = np.array([
    [80, 75, 90],
    [85, 95, 88],
    [70, 82, 78]
])

print("\n2D Array:")
print(students)


print("First row:", students[0])
print("Second row:", students[1])


print("First column:", students[:, 0])
print("Second column:", students[:, 1])


print("Element:", students[1, 2])



print("First two rows:")
print(students[0:2])

print("First two columns:")
print(students[:, 0:2])



print("Every second element:")
print(marks[::2])



print("Marks greater than 80:")
print(marks[marks > 80])