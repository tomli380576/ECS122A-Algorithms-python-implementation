import heapq
import random
from example_weighted_graphs import W_DIRECTED_1, W_DIRECTED_2, W_DIRECTED_3
from graph_helpers import InitializeSSSP, GetVertices, ConstructPath, Vertex, WeightedGraph, Number

# Avoid name clash with the library Priority Queue
PrioQueue = list[tuple[Number, Vertex]]


def UpdatePriority(queue: PrioQueue, vertex_to_update: Vertex,
                   new_prio: Number):
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


def Dijkstras(G: WeightedGraph, start: Vertex):
    dist, pred = InitializeSSSP(G, start)
    queue: PrioQueue = []

    heapq.heappush(queue, (0, start))

    while len(queue) > 0:
        _, u = heapq.heappop(queue)

        for weight, v in G[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
                if v in queue:
                    UpdatePriority(queue, v, dist[v])
                else:
                    heapq.heappush(queue, (dist[v], v))

    return dist, pred


if __name__ == '__main__':
    # Change these 2 variables to run on different graphs or run on all vertices
    run_on_all_vertices = False
    graph = W_DIRECTED_3

    if run_on_all_vertices:
        for start in GetVertices(graph):
            dist, pred = NonNegative_Dijkstras(graph, start)
            for end in GetVertices(graph):
                if end != start:
                    path = ConstructPath(pred, end)
                    if len(path) > 0:
                        print(f'Shortest Path from {start} to {end} is {path}')
                    else:
                        print(
                            f"\033[91mNo path from \'{start}\' to \'{end}\'\033[0m"
                        )
            print('==========================')
    else:
        start = random.choice(GetVertices(graph))
        print(f'==> Selected start: {start}')
        dist, pred = Dijkstras(graph, start)
        for end in GetVertices(graph):
            if end != start:
                path = ConstructPath(pred, end)
                if len(path) > 0:
                    print(f'Shortest Path from {start} to {end} is {path}')
                else:
                    print(
                        f"\033[91mNo path from \'{start}\' to \'{end}\'\033[0m"
                    )
