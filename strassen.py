import numpy as np
import time
import matplotlib.pyplot as plt

def my_matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def my_divide_and_conquer(matrix1, matrix2):
    n = len(matrix1)
    if n == 1:
        return matrix1 * matrix2
    
    half_size = n // 2

    a11, a12, a21, a22 = matrix1[:half_size, :half_size], matrix1[:half_size, half_size:], \
                         matrix1[half_size:, :half_size], matrix1[half_size:, half_size:]
    b11, b12, b21, b22 = matrix2[:half_size, :half_size], matrix2[:half_size, half_size:], \
                         matrix2[half_size:, :half_size], matrix2[half_size:, half_size:]

    c11 = my_divide_and_conquer(a11, b11) + my_divide_and_conquer(a12, b21)
    c12 = my_divide_and_conquer(a11, b12) + my_divide_and_conquer(a12, b22)
    c21 = my_divide_and_conquer(a21, b11) + my_divide_and_conquer(a22, b21)
    c22 = my_divide_and_conquer(a21, b12) + my_divide_and_conquer(a22, b22)

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

def my_strassen(matrix1, matrix2):
    n = len(matrix1)
    if n == 1:
        return matrix1 * matrix2
    a11, a12, a21, a22 = matrix1[:n//2, :n//2], matrix1[:n//2, n//2:], matrix1[n//2:, :n//2], matrix1[n//2:, n//2:]
    b11, b12, b21, b22 = matrix2[:n//2, :n//2], matrix2[:n//2, n//2:], matrix2[n//2:, :n//2], matrix2[n//2:, n//2:]
    p1 = my_strassen(a11 + a22, b11 + b22)
    p2 = my_strassen(a21 + a22, b11)
    p3 = my_strassen(a11, b12 - b22)
    p4 = my_strassen(a22, b21 - b11)
    p5 = my_strassen(a11 + a12, b22)
    p6 = my_strassen(a21 - a11, b11 + b12)
    p7 = my_strassen(a12 - a22, b21 + b22)
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6
    result_matrix = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return result_matrix

def generate_random_matrix(size):
    return np.random.randint(10, size=(size, size))

def measure_runtime(matrix_size, method):
    matrix1 = generate_random_matrix(matrix_size)
    matrix2 = generate_random_matrix(matrix_size)

    start_time = time.time()
    result = method(matrix1, matrix2)
    end_time = time.time()

    return end_time - start_time

matrix_sizes = [2**i for i in range(1, 8)]
my_multiplication_runtimes = []
my_divide_conquer_runtimes = []
my_strassen_runtimes = []

for size in matrix_sizes:
    runtime = measure_runtime(size, my_matrix_multiplication)
    my_multiplication_runtimes.append(runtime)

    runtime = measure_runtime(size, my_divide_and_conquer)
    my_divide_conquer_runtimes.append(runtime)

    runtime = measure_runtime(size, my_strassen)
    my_strassen_runtimes.append(runtime)

plt.plot(matrix_sizes, my_multiplication_runtimes, label='My Multiplication', marker='o')
plt.plot(matrix_sizes, my_divide_conquer_runtimes, label='My Divide and Conquer', marker='o')
plt.plot(matrix_sizes, my_strassen_runtimes, label='My Strassen Algorithm', marker='o')

plt.title('Matrix Multiplication Runtimes')
plt.xlabel('Size of matrix')
plt.ylabel('Runtime (seconds)')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()