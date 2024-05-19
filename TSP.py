import numpy as np

def bound(node, graph, visited):
    cost = 0
    for i in range(len(graph)):
        if i not in visited:
            min_edge = min(graph[node][j] for j in range(len(graph)) if j != node and j not in visited)
            cost += min_edge
    return cost

def tsp(graph):
    n = len(graph)
    best_cost = np.inf
    best_path = []

    pq = [(0, [0], set([0]))]  

    while pq:
        cost, path, visited = pq.pop(0)
        current_node = path[-1]

        if len(visited) == n:
            cost += graph[current_node][0]
            if cost < best_cost:
                best_cost = cost
                best_path = path
            continue
        lb = bound(current_node, graph, visited)
        if cost + lb >= best_cost:
            continue

        for next_node in range(n):
            if next_node not in visited:
                next_cost = cost + graph[current_node][next_node]
                pq.append((next_cost, path + [next_node], visited.union([next_node])))

        pq.sort(key=lambda x: x[0])

    return best_path, best_cost

graph = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 40],
    [20, 25, 30, 0, 45],
    [25, 30, 40, 45, 0]
]

best_path, best_cost = tsp(graph)
print("Best path:", best_path)
print("Best cost:", best_cost)
