import numpy as np


integer_array = np.array([10, 20, 30])

print("Integer:", integer_array)
print("Integer dtype:", integer_array.dtype)



float_array = np.array([10.5, 20.5, 30.5])

print("Float:", float_array)
print("Float dtype:", float_array.dtype)



boolean_array = np.array([True, False, True])

print("Boolean:", boolean_array)
print("Boolean dtype:", boolean_array.dtype)


complex_array = np.array([2+3j, 4+5j])

print("Complex:", complex_array)
print("Complex dtype:", complex_array.dtype)



string_array = np.array(["Python", "NumPy", "AI"])

print("String:", string_array)
print("String dtype:", string_array.dtype)


number_array = np.array([10, 20, 30], dtype=float)

print("Converted to Float:", number_array)
print("dtype:", number_array.dtype)



original_array = np.array([10.5, 20.5, 30.5])

integer_values = original_array.astype(int)

print("Original:", original_array)
print("Converted to Integer:", integer_values)