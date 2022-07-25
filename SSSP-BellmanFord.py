from example_weighted_graphs import W_DIRECTED_1, W_DIRECTED_2
from math import inf
import random
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


def ConstructPath(prev: dict[Vertex, Vertex], start: Vertex,
                  end: Vertex) -> list[Vertex]:
    if prev[end] == None:
        return []

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
                dist[v] = dist[u] + weight
                prev[v] = u
    '''
    Now there shouldn't be any tense edges,
    If we find any, then the graph has a negative cycle
    '''
    for edge in edges:
        weight, u, v = edge
        if dist[u] + weight < dist[v]:
            raise ValueError('Negative Cycle, No solution')

    print('No Cycles Found')

    return dist, prev


if __name__ == '__main__':
    run_on_all_vertices = False
    graph = W_DIRECTED_1

    if run_on_all_vertices:
        for start in GetVertices(graph):
            # start = '3'
            dist, prev = BellmanFord(graph, start)
            for end in GetVertices(graph):
                if end != start:
                    path = ConstructPath(prev, start, end)
                    if len(path) > 0:
                        print(f'Shortest Path from {start} to {end} is {path}')
                    else:
                        print(
                            f"\033[91mNo path from \'{start}\' to \'{end}\'\033[0m"
                        )
            print('=============')
    else:
        start = random.choice(GetVertices(graph))
        print(f'==> Selected start: {start}')
        dist, prev = BellmanFord(graph, start)
        for end in GetVertices(graph):
            if end != start:
                path = ConstructPath(prev, start, end)
                if len(path) > 0:
                    print(f'Shortest Path from {start} to {end} is {path}')
                else:
                    print(
                        f"\033[91mNo path from \'{start}\' to \'{end}\'\033[0m"
                    )
