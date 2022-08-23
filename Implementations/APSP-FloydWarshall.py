from example_weighted_graphs import W_DIRECTED_1, W_DIRECTED_2
from graph_helpers import WeightedGraph, Vertex
from math import inf


def FloydWarshall(G: WeightedGraph) -> dict[Vertex, dict[Vertex, int]]:
    dist = {v: {u: 0 for u in G.keys()} for v in G.keys()}

    for u in G.keys():
        for v in G.keys():
            if u == v:
                dist[u][v] = 0
                continue
            '''
            I know the filter thing looks kinda weird
            all it does is search through the adjacency list of u, finds v, take the weight
            first [0] is guaranteed (weight, v) because there are no duplicates,
            second [0] returns weight from the tuple
            '''
            uv_connected = len(list(filter(lambda item: item[1] == v,
                                           G[u]))) != 0
            if uv_connected:
                weight = list(filter(lambda item: item[1] == v, G[u]))[0][0]
                dist[u][v] = weight
            else:
                dist[u][v] = inf  # type: ignore

    # Main recurrence
    for r in G.keys():
        for u in G.keys():
            for v in G.keys():
                # if tense, relax
                if dist[u][v] > dist[u][r] + dist[r][v]:
                    dist[u][v] = dist[u][r] + dist[r][v]

    return dist


if __name__ == '__main__':
    dist = FloydWarshall(W_DIRECTED_2)
    '''
    Pretty Printing 2D Dict Driver Code

    How to read the matrix:
    Suppose we have this:
                S       A       B       C       D
        S       0       8       9       5       7
        ...other rows
    Then on row 'S' at column 'A' is the length of the shorest path from S to A
    Here it's 8
    '''
    print('\n')
    for key in dist.keys():
        print(f'\t{key}', end='')
    print('\n')
    for idx, u in enumerate(dist.keys()):
        print(f'{u}', end='')
        for v in dist.keys():
            print(f'\t{dist[u][v]}', end='')
        print('\n')