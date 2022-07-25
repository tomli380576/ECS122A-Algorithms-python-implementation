import heapq
import random
from example_weighted_graphs import W_DIRECTED_1, W_DIRECTED_2
from math import inf
'''
Types
'''
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
    if start not in vertices:
        raise ValueError(
            f'\033[94mVertex {start} is not in the graph. \033[0m')

    dist = {vertex: inf for vertex in vertices}
    pred = {vertex: None for vertex in vertices}
    dist[start] = 0

    return dist, pred


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


def UpdatePriority(queue, vertex_to_update: Vertex, new_prio: int):
    '''
    This looks pretty cumbersome because the heapq library doesn't support direct updates
    If you implement a custom priority queue it should be O(log n) update
    Here it's O(n) + O(log n) = O(n)
    '''
    for i in range(len(queue)):
        _, v = queue[i]
        if v == vertex_to_update:
            queue[i] = (new_prio, v)
            heapq.heapify(queue)
            return


def NonNegative_Dijkstras(G: Graph, start: Vertex):
    dist, pred = InitializeSSSP(G, start)
    vertices = GetVertices(G)
    queue: list[tuple[int, Vertex]] = []

    for vertex in vertices:
        heapq.heappush(queue, (dist[vertex], vertex))

    while len(queue) > 0:
        _, u = heapq.heappop(queue)
        '''
        For each adjacent vertex to u, if tense, relax and update priority
        '''
        for weight, adj_vertex in G[u]:
            if dist[u] + weight < dist[adj_vertex]:
                dist[adj_vertex] = dist[u] + weight
                pred[adj_vertex] = u
                UpdatePriority(queue, adj_vertex, dist[adj_vertex])

    return dist, pred


if __name__ == '__main__':
    run_on_all_vertices = False
    graph = W_DIRECTED_2

    if run_on_all_vertices:
        for start in GetVertices(graph):
            # start = '3'
            dist, prev = NonNegative_Dijkstras(graph, start)
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
        dist, prev = NonNegative_Dijkstras(graph, start)
        for end in GetVertices(graph):
            if end != start:
                path = ConstructPath(prev, start, end)
                if len(path) > 0:
                    print(f'Shortest Path from {start} to {end} is {path}')
                else:
                    print(
                        f"\033[91mNo path from \'{start}\' to \'{end}\'\033[0m"
                    )
