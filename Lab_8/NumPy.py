import numpy as np

# 1. Create an array of 10 zeros
array_zeros = np.zeros(10)
print("Array of 10 zeros:", array_zeros)

# 2. Create an array of 10 ones
array_ones = np.ones(10)
print("Array of 10 ones:", array_ones)

# 3. Create an array of 10 fives
array_fives = np.ones(10) * 5
print("Array of 10 fives:", array_fives)

# 4. Create an array of the integers from 10 to 50
array_integers = np.arange(10, 51)
print("Array of integers from 10 to 50:", array_integers)

# 5. Create an array of all the even integers from 10 to 50
array_even_integers = np.arange(10, 51, 2)
print("Array of even integers from 10 to 50:", array_even_integers)

# 6. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 matrix with values from 0 to 8:\n", matrix_3x3)

# 7. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("3x3 identity matrix:\n", identity_matrix)

# 8. Use NumPy to generate a random number between 0 and 1
random_number = np.random.rand(1)
print("Random number between 0 and 1:", random_number)

# 9. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
random_array = np.random.randn(25)
print("Array of 25 random numbers from standard normal distribution:\n", random_array)

# 10. Create the specified matrix
matrix_specified = np.arange(1, 101).reshape(10, 10) / 100
print("Specified matrix:\n", matrix_specified)

# 11. Create an array of 20 linearly spaced points between 0 and 1
linear_spaced_array = np.linspace(0, 1, 20)
print("Array of 20 linearly spaced points between 0 and 1:", linear_spaced_array)

# Numpy Indexing and Slicing
mat = np.arange(1, 26).reshape(5, 5)
print("Original matrix:\n", mat)

# 12. Slice out a section
section = mat[2:, 1:]
print("Sliced section:\n", section)

# 13. Get element at specific index
element = mat[3, 4]
print("Element at specific index:", element)

# 14. Get column from a specific row range
column_section = mat[:3, 1:2]
print("Column from specific row range:\n", column_section)

# 15. Get row
row_section = mat[4, :]
print("Row section:", row_section)

# 16. Get last two rows
last_two_rows = mat[3:, :]
print("Last two rows:\n", last_two_rows)

# 17. Print all numbers divisible by 3 but not by 5
divisible_by_3_not_5 = mat[(mat % 3 == 0) & (mat % 5 != 0)]
print("Numbers divisible by 3 but not by 5:", divisible_by_3_not_5)

# 18. Sum of all values in mat
sum_values = np.sum(mat)
print("Sum of all values in mat:", sum_values)

# 19. Standard deviation of values in mat
std_deviation = np.std(mat)
print("Standard deviation of values in mat:", std_deviation)

# 20. Sum of all columns in mat
sum_columns = np.sum(mat, axis=0)
print("Sum of all columns in mat:", sum_columns)
