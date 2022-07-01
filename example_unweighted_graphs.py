# All the example unweighted graphs

DIRECTED_1: dict[str, list[str]] = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

UNDIRECTED_1: dict[str, list[str]] = {
    '5': ['3', '7'],
    '3': ['2', '4', '5'],
    '7': ['8', '5'],
    '2': ['3'],
    '4': ['8', '3'],
    '8': ['4', '7']
}

UNDIRECTED_2: dict[str, list[str]] = {
    'A': ['B', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'E': ['A', 'C'],
    'D': ['B', 'C']
}

UNDIRECTED_3: dict[str, list[str]] = {
    'S': ['A', 'C', 'G'],
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'H', 'S'],
    'H': ['E', 'G']
}