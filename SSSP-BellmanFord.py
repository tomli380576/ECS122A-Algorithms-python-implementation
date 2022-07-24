from example_weighted_graphs import W_DIRECTED_1
from math import inf
'''Types'''
Vertex = str
Edge = tuple[int, Vertex, Vertex]
Graph = dict[str, list[tuple[int, str]]]


def GetVertices(G: Graph) -> list[Vertex]:
    return list(G.keys())


def GetEdges(G: Graph) -> list[Edge]:
    out: list[Edge] = []
    for vertex, adj_list in G.items():
        for adj_vertex in adj_list:
            out.append((adj_vertex[0], vertex, adj_vertex[1]))
    return out


def InitializeSSSP(G: Graph, start: Vertex) -> tuple[dict, dict]:
    vertices = GetVertices(G)
    assert (start in vertices)

    dist = {vertex: inf for vertex in vertices}
    prev = {vertex: None for vertex in vertices}
    dist[start] = 0

    return dist, prev


def ConstructPath(prev: dict[Vertex, Vertex], end: Vertex) -> list[Vertex]:
    curr = prev[end]
    path = [end]
    '''
    It's like traversing a linked list
    '''
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    '''we appended everything to the back, so reverse it'''
    path.reverse()
    return path


def BellmanFord(G: Graph, start: Vertex):
    dist, prev = InitializeSSSP(G, start)
    num_vertices = len(GetVertices(G))
    edges = GetEdges(G)

    '''
    Underscore means we don't use this variable
    '''
    for _ in range(num_vertices - 1):
        for edge in edges:
            weight, u, v = edge
            '''
            If tense, relax it
            '''
            if dist[u] + weight < dist[v]:
                print(f'Relaxed edge {u} -> {v} from {dist[v]} to {dist[u] + weight}')
                dist[v] = dist[u] + weight
                prev[v] = u

    '''
    Now there shouldn't be any tense edges,
    If we find any, then the graph has a negative cycle
    '''
    print('Main loop over, checking for cycles')
    for edge in edges:
        weight, u, v = edge
        if dist[u] + weight < dist[v]:
            raise ValueError('Negative Cycle, No solution')

    return dist, prev


if __name__ == '__main__':
    start = 'S'
    dist, prev = BellmanFord(W_DIRECTED_1, start)
    for vertex in GetVertices(W_DIRECTED_1):
        if vertex != start:
            print(
                f'Shortest Path from {start} to {vertex} is {ConstructPath(prev, vertex)}'
            )
