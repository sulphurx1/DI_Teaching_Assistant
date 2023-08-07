import numpy as np

data = np.array(np.random.randint(1, 100, size=25)).reshape(5,5)
print(data)

# 1. Matrix manipulation - Swap the second and fourth rows of the data matrix.
data[[1, 3]] = data[[3, 1]]
print(data)

# 2. Normalize all the elements in the data matrix such that they are scaled to range between 0 and 1. Hint: to normalize, subtract the minimum and divide by the max-min.
min_val = np.min(data)
max_val = np.max(data)

normalize  = np.round((data - min_val) / (max_val - min_val), 2)
# other option
# np.set_printoptions(precision=2, suppress=True)
print(normalize)

# 3. Z-score normalization - Standardize the data matrix using Z-score normalization. That is, all the elements should be scaled to have a mean* of 0 and a standard deviation of 1. Z-score is calculated as (X - mean) / std.
z_score_normalize = np.round((data - np.mean(data)) / np.std(data), 2)
print(z_score_normalize)

# 4. Array splitting - Reshape the data matrix into a vector (Hint: use np.ravel) and split this array into five equal-sized sub-arrays.
ravel_data = np.ravel(data)
array_split = np.split(ravel_data, 5)

print(array_split)

# 5. Dot product - Create two vectors of size 5 with any values. Compute the dot product of the two vectors*.
v1 = [3, 5, 6, 7, 8]
v2 = [2, 4, 6, 8, 10]
dot_product = np.dot(v1, v2)
print(dot_product)

# 6.Matrix multiplication - Create another 3x3 matrix with any values (let’s call it data2). Perform matrix multiplication (dot product of data (first 3x3 part) and data2).
data1 = np.array(np.random.randint(10, size=(3, 3)))


matrix_mul = np.matmul(data[:3, :3], data1)
print(matrix_mul)

# 7. Inverse of a matrix - Create a 3x3 identity matrix*, multiply it with 2 and compute its inverse.
I = np.identity(3)
I_2 = np.linalg.inv(I * 2)
print(I_2)

# 8. Eigenvalues and eigenvectors - For the first 3x3 part of the data matrix, compute the eigenvalues and eigenvectors*.
eigenvalues, eigenvectors = np.linalg.eig(data[:3, :3])
np.set_printoptions(precision=2, suppress=True)
print(eigenvalues, eigenvectors)

# 9. Find missing values - Replace random 5 elements in the data matrix with np.nan. Find the indices of the missing values.
data3 = np.random.rand(5, 5)
missing_values =  np.random.choice(data3.size, 5)
data3.ravel()[missing_values] = np.nan

arrays = np.where(np.isnan(data3))

print(arrays)
# 10. Replace missing values - Replace the missing values in the data matrix with the mean of the matrix (ignoring the missing values while computing the mean).
mean_values = np.mean(data)
data[np.isnan(data)] = mean_values
print(data)