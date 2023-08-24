# 1. Import the numpy package under the name np.
import numpy as np

# 2. Create a vector* of zeros with size 10 using np.zeros().
vector_1 = np.zeros(10)

# 3. Compute the memory size* of any array. Note: You can do this by multiplying the length of the array by the size of one array element, which you can find using the .itemsize attribute.
memory_size = vector_1.size * vector_1.itemsize
print(memory_size)

# 4. Retrieve the documentation of the numpy add function from the command line.
# help(np.add)

# 5. Create a vector with values ranging from 10 to 49 using np.arange().
vector_2 = np.arange(10, 50, 1, dtype=int)
print(vector_2)

# 6. Reverse a vector so the first element becomes last (Hint: Use slicing).
vector_3 = vector_2[::-1]
print(vector_3)

# 7. Create a 3x3 matrix* with values ranging from 0 to 8 using np.reshape().
a = np.arange(9).reshape((3, 3))
print(a)

# 8. Find indices of non-zero elements from [1,2,0,0,4,0] using np.nonzero().
y = [1,2,0,0,4,0]
z = np.nonzero(y)
print(z)

# 9. Create a 3x3 identity matrix* using np.eye().
b = np.eye(3, k=1)
print(b)

# 10. Create a 5x5 matrix with row values ranging from 0 to 4. The output should be a matrix where each row is [0, 1, 2, 3, 4].
matrix = np.tile(np.arange(5), (5, 1))
print(matrix)