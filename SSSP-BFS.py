from queue import Queue
from example_unweighted_graphs import UNDIRECTED_3
from SSSP_graph_helpers import InitializeSSSP, GetVertices, ConstructPath, Vertex, UnweightedGraph


def BFS_SSSP_Unweighted(G: UnweightedGraph, start: Vertex):
    dist, prev = InitializeSSSP(G, start)
    queue: Queue[Vertex] = Queue()
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
    start: Vertex = 'S'
    dist, prev = BFS_SSSP_Unweighted(UNDIRECTED_3, start)
    print(f'dist:{dist}\nprev:{prev}\n======')

    for vertex in GetVertices(UNDIRECTED_3):
        if vertex != start:
            print(
                f'Shortest Path from {start} to {vertex} is {ConstructPath(prev, vertex)}'
            )
