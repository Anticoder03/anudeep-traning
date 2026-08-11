import numpy as np
print(np.__version__)
a = [[1,2,3],[4,5,6]]
print(a[1][1])


print("Mean:", np.mean(a))
print("Median:", np.median(a))

# practice functions
print("Standard Deviation:", np.std(a))

# zeroes
print("Zeroes:", np.zeros((2, 3)))

# arrange
print("Arrange:", np.arange(0, 10, 2))

identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)


# size
print("Size of array:", np.size(a))

# random
random_array = np.random.rand(2, 3)
print("Random Array:\n", random_array)

base = np.array([1,2,3,4,5,6,7,8,9,10])

sq = np.square(base)
print("Square of base array:", sq)

sqrt_array = np.sqrt(sq)
print("Square root of base array:", sqrt_array)

# argmin
argmin_index = np.argmin(base)
print("Index of minimum value in base array:", argmin_index)

# argmax
argmax_index = np.argmax(base)

print("Index of maximum value in base array:", argmax_index)

# reshape
reshaped_array = np.reshape(base, (2, 5))
print("Reshaped Array:\n", reshaped_array)

# flaten
flattened_array = np.ravel(reshaped_array)
print("Flattened Array:", flattened_array)

# without inbuilt functions 2d to 1d
def flatten_2d_to_1d(array_2d):
    flattened = []
    for row in array_2d:
        for element in row:
            flattened.append(element)
    return flattened

flattened_custom = flatten_2d_to_1d(reshaped_array)
print("Flattened Array using custom function:", flattened_custom)