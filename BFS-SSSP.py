from math import inf
from queue import Queue
from example_unweighted_graphs import UNDIRECTED_3

Vertex = str
Graph = dict[str, list[str]]


def GetVertices(G: Graph) -> list[Vertex]:
    return list(G.keys())


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

    path.reverse()
    return path


def BFS_SSSP_Unweighted(G: Graph, start: Vertex) -> tuple[dict, dict]:
    dist, prev = InitializeSSSP(G, start)
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        u = queue.get()
        for adjacent_vertex in G[u]:
            '''
            if the edge is tense
            - weight is 1 for unweighted graphs
            '''
            if dist[u] + 1 < dist[adjacent_vertex]:
                '''
                RelaxEdge()
                '''
                dist[adjacent_vertex] = dist[u] + 1
                prev[adjacent_vertex] = u
                queue.put(adjacent_vertex)

    return dist, prev


if __name__ == '__main__':
    start_vertex = 'S'
    dist, prev = BFS_SSSP_Unweighted(UNDIRECTED_3, start_vertex)
    print(f'dist:{dist}\nprev:{prev}\n')

    for vertex in GetVertices(UNDIRECTED_3):
        if vertex != start_vertex:
            print(
                f'Shortest Path from {start_vertex} to {vertex} is {ConstructPath(prev, vertex)}'
            )