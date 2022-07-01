import math
from queue import Queue
from example_unweighted_graphs import UNDIRECTED_3


def GetVertices(G: dict[str, list[str]]) -> list[str]:
    return list(G.keys())


def InitializeSSSP(G: dict[str, list[str]],
                   start_vertex: str) -> tuple[dict, dict]:
    vertices = GetVertices(G)
    assert (start_vertex in vertices)

    dist = {vertex: math.inf for vertex in vertices}
    prev = {vertex: None for vertex in vertices}
    dist[start_vertex] = 0

    return dist, prev


def ConstructPath(end_vertex: str, prev: dict):
    # Assert that prev is 1 dimensional
    curr = prev[end_vertex]
    path = [end_vertex]

    # Since the prev array contains both prev nodes and nan
    # We havd to cast node values to integer to be used as index
    # can be avoided with python dicts
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return path


def BFS_SSSP(G: dict[str, list[str]], start_vertex: str):
    dist, prev = InitializeSSSP(G, start_vertex)
    queue = Queue()
    queue.put(start_vertex)
    while not queue.empty():
        u = queue.get()
        for adjacent_vertex in G[u]:
            # if connected
            # if Tense, since it's unweighted we can let all weighte be 1
            if dist[u] + 1 < dist[adjacent_vertex]:
                # Relax
                dist[adjacent_vertex] = dist[u] + 1
                prev[adjacent_vertex] = u
                # push into queue
                queue.put(adjacent_vertex)
    return dist, prev


if __name__ == '__main__':
    start_vertex = 'S'
    dist, prev = BFS_SSSP(UNDIRECTED_3, start_vertex)
    print(f'dist:{dist}, prev:{prev}')
    for vertex in GetVertices(UNDIRECTED_3):
        if vertex != start_vertex:
            print(
                f'Shortest Path from {start_vertex} to {vertex} is {ConstructPath(vertex, prev)}'
            )
