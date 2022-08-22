from math import inf
from example_weighted_graphs import W_DIRECTED_1
from graph_helpers import WeightedGraph, GetWeightedEdges


def APSPBellmanFord(G: WeightedGraph):
    dist = {v: {u: 0 for u in G.keys()} for v in G.keys()}

    # Fill in base cases
    for u in G.keys():
        for v in G.keys():
            if u == v:
                dist[u][v] = 0
            else:
                dist[u][v] = inf  # type: ignore

    # Iterate over all u and edges
    for max_edges in range(len(G.keys()) - 1):
        for u in G.keys():
            for edge in GetWeightedEdges(G):
                weight, x, v = edge
                # if tense
                if dist[u][v] > dist[u][x] + weight:
                    # Relax
                    dist[u][v] = dist[u][x] + weight

    return dist


if __name__ == '__main__':
    dist = APSPBellmanFord(W_DIRECTED_1)

    # Pretty Printing 2D Dict Driver Code
    print('\n')
    for key in dist.keys():
        print(f'\t{key}', end='')
    print('\n')
    for idx, u in enumerate(dist.keys()):
        print(f'{u}', end='')
        for v in dist.keys():
            print(f'\t{dist[u][v]}', end='')
        print('\n')
    '''
    How to read the matrix:
    Suppose we have this:
                S       A       B       C       D
        S       0       8       9       5       7
        ...other rows
    Then on row 'S' at column 'A' is the length of the shorest path from S to A
    Here it's 8
    '''
