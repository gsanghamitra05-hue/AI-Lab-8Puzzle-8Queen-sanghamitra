from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
min_cost = float('inf')

for path in permutations(range(1, n)):
    route = (0,) + path + (0,)
    cost = sum(dist[route[i]][route[i+1]]
               for i in range(n))

    if cost < min_cost:
        min_cost = cost
        best_route = route

print("Shortest Route:", best_route)
print("Minimum Cost:", min_cost)
