import numpy as np

WeightedGraph = dict[str, list[tuple[int, str]]]

# TODO: change to adjacency list
W_UNDIRECTED_1 = np.array([[0, 9, 75, 0, 0], [9, 0, 95, 19, 42],
                           [75, 95, 0, 51, 66], [0, 19, 51, 0, 31],
                           [0, 42, 66, 31, 0]])

W_DIRECTED_1: WeightedGraph = {
    'S': [(10, 'A'), (5, 'C')],
    'A': [(2, 'C'), (1, 'B')],
    'B': [(4, 'D')],
    'C': [(3, 'A'), (9, 'B'), (2, 'D')],
    'D': [(7, 'S'), (6, 'B')]
}

W_DIRECTED_2: WeightedGraph = {
    '1': [],
    '2': [(4, '1')],
    '3': [(5, '1'), (6, '2'), (4, '4')],
    '4': [
        (3, '3'),
        (3, '2'),
        (4, '5'),
    ],
    '5': [(10, '2'), (6, '4'), (2, '6')],
    '6': [
        (9, '3'),
        (3, '4'),
        (3, '5'),
    ],
    '7': [(2, '5'), (2, '6')],
}

W_DIRECTED_3: WeightedGraph = {
    'A': [(5, 'B'), (2, 'C')],
    'B': [(-10, 'C')],
    'C': []
}
