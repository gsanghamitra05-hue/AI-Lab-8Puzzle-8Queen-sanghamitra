colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

result = {}

def color_map(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for color in colors:
        if all(result.get(n) != color for n in graph[region]):
            result[region] = color

            if color_map(node + 1):
                return True

            del result[region]

    return False

if color_map(0):
    print("Map Coloring:")
    print(result)
else:
    print("No solution")
