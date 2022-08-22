# All the example unweighted graphs
UnweightedGraph = dict[str, list[str]]

DIRECTED_1: UnweightedGraph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

DIRECTED_ACYCLIC_1: UnweightedGraph = {
    'A': ['C'],
    'B': ['C', 'E'],
    'C': ['D'],
    'D': [],
    'E': ['D']
}
DIRECTED_ACYCLIC_2: UnweightedGraph = {
    '5': ['2', '0'],
    '4': ['0', '1'],
    '3': ['1'],
    '2': ['3'],
    '1': [],
    '0': []
}

DIRECTED_CYCLIC_1: UnweightedGraph = {
    '5': ['7'],
    '3': ['2', '4', '5'],
    '7': ['8'],
    '2': [],
    '4': ['3', '8'],
    '8': []
}

DIRECTED_CYCLIC_2: UnweightedGraph = {
    'S': ['T'],
    'T': ['U', 'V'],
    'U': ['S', 'V', 'W'],
    'V': [],
    'W': ['V'],
}

UNDIRECTED_1: UnweightedGraph = {
    '5': ['3', '7'],
    '3': ['2', '4', '5'],
    '7': ['8', '5'],
    '2': ['3'],
    '4': ['8', '3'],
    '8': ['4', '7']
}

UNDIRECTED_2: UnweightedGraph = {
    'A': ['B', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'E': ['A', 'C'],
    'D': ['B', 'C']
}

UNDIRECTED_3: UnweightedGraph = {
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