import numpy as np

def distance_calculator(tour, matrix_distance):
    distance = 0
    n = len(tour)
    for i in range(n - 1):
        distance += matrix_distance[tour[i]][tour[i + 1]]
    distance += matrix_distance[tour[-1]][tour[0]] 
    return distance

def generate_random_tour(n):
    return np.random.permutation(n)

def monte_carlo_tsp(matrix_distance, iterations):
    n = len(matrix_distance)
    best_tour = None
    best_distance = np.inf

    for _ in range(iterations):
        tour = generate_random_tour(n)
        distance = distance_calculator(tour, matrix_distance)
        if distance < best_distance:
            best_distance = distance
            best_tour = tour

    return best_tour, best_distance

# New matrix_distance
matrix_distance = [
    [0, 10, 15, 20, 12],
    [10, 0, 35, 25, 28],
    [15, 35, 0, 30, 18],
    [20, 25, 30, 0, 22],
    [12, 28, 18, 22, 0]
]
iterations = 10000

best_tour, best_distance = monte_carlo_tsp(matrix_distance, iterations)
print("Best tour is: ", best_tour)
print("Best distance is: ", best_distance)