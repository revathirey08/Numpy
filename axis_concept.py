import numpy as np

marks = np.array([
    [80, 70, 90],
    [85, 75, 95],
    [60, 80, 70]
])

print("Marks:")
print(marks)



print("\nSum using Axis 0:")
print(np.sum(marks, axis=0))



print("\nSum using Axis 1:")
print(np.sum(marks, axis=1))



print("\nMean using Axis 0:")
print(np.mean(marks, axis=0))



print("\nMean using Axis 1:")
print(np.mean(marks, axis=1))



print("\nMaximum using Axis 0:")
print(np.max(marks, axis=0))



print("\nMaximum using Axis 1:")
print(np.max(marks, axis=1))



print("\nMinimum using Axis 0:")
print(np.min(marks, axis=0))



print("\nMinimum using Axis 1:")
print(np.min(marks, axis=1))



students = np.array([
    [
        [80, 70, 90],
        [85, 75, 95]
    ],
    [
        [60, 80, 70],
        [90, 85, 88]
    ]
])

print("\n3D Array:")
print(students)


print("\n3D Sum Axis 0:")
print(np.sum(students, axis=0))


print("\n3D Sum Axis 1:")
print(np.sum(students, axis=1))

print("\n3D Sum Axis 2:")
print(np.sum(students, axis=2))