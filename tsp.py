
from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
start = 0
best_cost = float('inf')
best_path = []

for route in permutations(range(1, n)):
    path = (start,) + route + (start,)
    total = 0

    for i in range(len(path) - 1):
        total += cost[path[i]][path[i + 1]]

    if total < best_cost:
        best_cost = total
        best_path = path

print("Best path:", " -> ".join(str(x) for x in best_path))
print("Minimum cost:", best_cost)