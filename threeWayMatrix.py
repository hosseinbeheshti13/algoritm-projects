import numpy as np
import time
import matplotlib.pyplot as plt

def standard_multiply(A, B):
    return np.dot(A, B)

def strassen_multiply(A, B):
    if len(A) == 1:
        return A * B  # Base case for 1x1 matrices

    n = len(A) // 2
    A11, A12 = A[:n, :n], A[:n, n:]
    A21, A22 = A[n:, :n], A[n:, n:]
    B11, B12 = B[:n, :n], B[:n, n:]
    B21, B22 = B[n:, :n], B[n:, n:]

    # Strassen's algorithm
    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)

    # Compute the four submatrices of the result matrix
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6

    result_matrix = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result_matrix

def winograd_multiply(A, B):
    n = len(A)
    if n == 1:
        return A * B  # Base case for 1x1 matrices

    # Ensure that the matrix size is even
    if n % 2 != 0:
        raise ValueError("Matrix size must be even for Winograd's algorithm")

    m = n // 2  # New matrix size

    # Matrices split into four blocks
    A11, A12 = A[:m, :m], A[:m, m:]
    A21, A22 = A[m:, :m], A[m:, m:]
    B11, B12 = B[:m, :m], B[:m, m:]
    B21, B22 = B[m:, :m], B[m:, m:]

    # Intermediate matrices
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12

    # Intermediate results
    P1 = winograd_multiply(A11, S1)
    P2 = winograd_multiply(S2, B22)
    P3 = winograd_multiply(S3, B11)
    P4 = winograd_multiply(A22, S4)
    P5 = winograd_multiply(S5, S6)
    P6 = winograd_multiply(S7, S8)
    P7 = winograd_multiply(S9, S10)

    # Compute the four submatrices of the result matrix
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    result_matrix = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result_matrix

# Function to calculate time complexity T(n)
def time_complexity(n, algorithm):
    if algorithm == 'standard':
        return n**3
    elif algorithm == 'strassen':
        return n**(np.log2(7))
    elif algorithm == 'winograd':
        return n**(np.log2(21))

# Matrix sizes to compare
matrix_sizes = [2, 4, 8, 16, 32, 64, 128]

# Lists to store execution times
execution_times_standard = []
execution_times_strassen = []
execution_times_winograd = []

# Algorithm names
algorithms = ['standard', 'strassen', 'winograd']

# Loop over different matrix sizes
for size in matrix_sizes:
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    # Time complexity for the specific matrix size
    time_complexity_size = time_complexity(size, 'standard')

    # Measure execution time for each algorithm
    start_time_standard = time.time()
    result_standard = standard_multiply(A, B)
    end_time_standard = time.time()
    execution_time_standard = end_time_standard - start_time_standard
    execution_times_standard.append(execution_time_standard)

    start_time_strassen = time.time()
    result_strassen = strassen_multiply(A, B)
    end_time_strassen = time.time()
    execution_time_strassen = end_time_strassen - start_time_strassen
    execution_times_strassen.append(execution_time_strassen)

    start_time_winograd = time.time()
    result_winograd = winograd_multiply(A, B)
    end_time_winograd = time.time()
    execution_time_winograd = end_time_winograd - start_time_winograd
    execution_times_winograd.append(execution_time_winograd)

# Plotting the execution times
plt.plot(matrix_sizes, execution_times_standard, label='Standard Multiplication')
plt.plot(matrix_sizes, execution_times_strassen, label="Strassen's Multiplication")
plt.plot(matrix_sizes, execution_times_winograd, label="Winograd's Multiplication")
plt.xscale('log', base=2)
plt.yscale('log')
plt.xlabel('Matrix Size (log scale)')
plt.ylabel('Execution Time (log scale)')
plt.title('Matrix Multiplication Algorithms for Different Matrix Sizes')
plt.legend()
plt.show()





