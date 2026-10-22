def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start)]
    g_cost = {start: 0}
    parent = {}

    while open_list:
        open_list.sort()
        f, current = open_list.pop(0)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]

        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current
                open_list.append(
                    (new_cost + heuristic[neighbor], neighbor)
                )

    return None, float("inf")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

path, cost = astar(graph, heuristic, 'A', 'D')

print("Shortest Path:", path)
print("Total Cost:", cost)
