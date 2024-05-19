import numpy as np
import time

def multiple_standard_way(A, B):
    return np.dot(A, B)

def multiple_strassen(A, B):
    if len(A) == 1:
        return A * B  

    n = len(A) // 2
    A11, A12 = A[:n, :n], A[:n, n:]
    A21, A22 = A[n:, :n], A[n:, n:]
    B11, B12 = B[:n, :n], B[:n, n:]
    B21, B22 = B[n:, :n], B[n:, n:]

    # Strassen's algorithm
    M1 = multiple_strassen(A11 + A22, B11 + B22)
    M2 = multiple_strassen(A21 + A22, B11)
    M3 = multiple_strassen(A11, B12 - B22)
    M4 = multiple_strassen(A22, B21 - B11)
    M5 = multiple_strassen(A11 + A12, B22)
    M6 = multiple_strassen(A21 - A11, B11 + B12)
    M7 = multiple_strassen(A12 - A22, B21 + B22)
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6

    result_matrix = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result_matrix

def multiple_wingrad(A, B):
    n = len(A)
    if n == 1:
        return A * B  
    if n % 2 != 0:
        raise ValueError("Matrix size must be even for Winograd's algorithm")

    m = n // 2  
    A11, A12 = A[:m, :m], A[:m, m:]
    A21, A22 = A[m:, :m], A[m:, m:]
    B11, B12 = B[:m, :m], B[:m, m:]
    B21, B22 = B[m:, :m], B[m:, m:]
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
    P1 = multiple_wingrad(A11, S1)
    P2 = multiple_wingrad(S2, B22)
    P3 = multiple_wingrad(S3, B11)
    P4 = multiple_wingrad(A22, S4)
    P5 = multiple_wingrad(S5, S6)
    P6 = multiple_wingrad(S7, S8)
    P7 = multiple_wingrad(S9, S10)
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    result_matrix = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result_matrix
def time_complexity(n, algorithm):
    if algorithm == 'standard':
        return n**3
    elif algorithm == 'strassen':
        return n**(np.log2(7))
    elif algorithm == 'winograd':
        return n**(np.log2(21))
try:
    size = int(input("Enter the size of the square matrices: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for matrix size.")
    exit()
A = np.random.rand(size, size)
B = np.random.rand(size, size)
if A.shape[0] % 2 != 0 or A.shape[1] % 2 != 0 or B.shape[0] % 2 != 0 or B.shape[1] % 2 != 0:
    raise ValueError("Matrix size must be even for Strassen's and Winograd's algorithms")

start_time_standard = time.time()
result_standard = multiple_standard_way(A, B)
end_time_standard = time.time()
execution_time_standard = end_time_standard - start_time_standard
time_complexity_standard = time_complexity(size, 'standard')

start_time_strassen = time.time()
result_strassen = multiple_strassen(A, B)
end_time_strassen = time.time()
execution_time_strassen = end_time_strassen - start_time_strassen
time_complexity_strassen = time_complexity(size, 'strassen')

start_time_winograd = time.time()
result_winograd = multiple_wingrad(A, B)
end_time_winograd = time.time()
execution_time_winograd = end_time_winograd - start_time_winograd
time_complexity_winograd = time_complexity(size, 'winograd')

print("\nMatrix A ({}x{}):".format(size, size))
print(A)

print("\nMatrix B ({}x{}):".format(size, size))
print(B)

print("\nResult of Standard Matrix Multiplication:")
print(result_standard)
print("\nExecution Time (Standard): {:.6f} seconds".format(execution_time_standard))
print("Time Complexity (Standard):", time_complexity_standard)

print("\nResult of Strassen's Matrix Multiplication:")
print(result_strassen)
print("\nExecution Time (Strassen): {:.6f} seconds".format(execution_time_strassen))
print("Time Complexity (Strassen):", time_complexity_strassen)

print("\nResult of Winograd's Matrix Multiplication:")
print(result_winograd)
print("\nExecution Time (Winograd): {:.6f} seconds".format(execution_time_winograd))
print("Time Complexity (Winograd):", time_complexity_winograd)

print("\nElement-wise comparison:")
print(np.allclose(result_standard, result_strassen, atol=1e-10) and np.allclose(result_standard, result_winograd, atol=1e-10))

