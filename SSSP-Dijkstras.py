import heapq
import random
from example_weighted_graphs import W_DIRECTED_1, W_DIRECTED_2
from SSSP_graph_helpers import InitializeSSSP, GetVertices, ConstructPath, Vertex, WeightedGraph

# Avoid name clash with the library Priority Queue
PrioQueue = list[tuple[int, Vertex]]

def UpdatePriority(queue: PrioQueue, vertex_to_update: Vertex,
                   new_prio: int):
    '''
    This looks pretty cumbersome because the heapq library doesn't support direct updates
    If you implement a custom priority queue it should be O(log n) update
    Here it's O(n) + O(log n) = O(n)
    '''
    for i in range(len(queue)):
        _, vertex = queue[i]
        if vertex == vertex_to_update:
            queue[i] = (new_prio, vertex)
            heapq.heapify(queue)
            return


def NonNegative_Dijkstras(G: WeightedGraph, start: Vertex):
    dist, pred = InitializeSSSP(G, start)
    vertices = GetVertices(G)
    queue: PrioQueue = []

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
    # Change these 2 variables to run on different graphs or run on all vertices
    run_on_all_vertices = False
    graph = W_DIRECTED_2

    if run_on_all_vertices:
        for start in GetVertices(graph):
            dist, prev = NonNegative_Dijkstras(graph, start)
            for end in GetVertices(graph):
                if end != start:
                    path = ConstructPath(prev, end)
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
                path = ConstructPath(prev, end)
                if len(path) > 0:
                    print(f'Shortest Path from {start} to {end} is {path}')
                else:
                    print(
                        f"\033[91mNo path from \'{start}\' to \'{end}\'\033[0m"
                    )
