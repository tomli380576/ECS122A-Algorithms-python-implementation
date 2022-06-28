from queue import PriorityQueue
import math
import numpy as np

SAMPLE_WEIGHTED_UNDIRECTED_GRAPH = np.array([[0, 9, 75, 0, 0],
                                             [9, 0, 95, 19, 42],
                                             [75, 95, 0, 51, 66],
                                             [0, 19, 51, 0, 31],
                                             [0, 42, 66, 31, 0]])

# TODO: Too much mess
def PrimsMST(G: np.ndarray) -> list:

    best_tree = []
    best_cost = math.inf
    for start_vertex in range(len(G)):

        priority_queue = PriorityQueue()
        curr_tree = [start_vertex]
        curr_cost = 0

        for adj_vertex in range(len(G[start_vertex])):
            # store as (weight, edge)
            if G[start_vertex][adj_vertex] != 0:  # is connected
                priority_queue.put((G[start_vertex][adj_vertex], adj_vertex))
        while not priority_queue.empty():
            min_vertex = priority_queue.get()[1]
            if min_vertex not in curr_tree:  # the edge is 'safe'
                curr_cost += G[curr_tree[len(curr_tree) - 1]][min_vertex]
                curr_tree.append(min_vertex)
                for adj_vertex in range(len(G[start_vertex])):
                    if G[min_vertex][adj_vertex] != 0:
                        priority_queue.put(
                            (G[min_vertex][adj_vertex], adj_vertex))

        if curr_cost < best_cost:
            best_tree = curr_tree
            best_cost = curr_cost

        print(curr_cost, curr_tree)
    return best_tree


def PrimsMST2(G: np.ndarray):

    # get the minimum edge of the entire graph
    def getMinWeightEdge():
        valid_idx_y, valid_idx_x = np.where(
            SAMPLE_WEIGHTED_UNDIRECTED_GRAPH > 0)
        minidx_both_axis = np.argmin(
            SAMPLE_WEIGHTED_UNDIRECTED_GRAPH[valid_idx_y, valid_idx_x])
        return (valid_idx_y[minidx_both_axis], valid_idx_x[minidx_both_axis])

    priority_queue = PriorityQueue()
    start_vertex = getMinWeightEdge()[0]
    curr_tree: list[tuple] = [start_vertex]

    for adj_vertex in range(len(G[start_vertex])):
        # store as (weight, edge)
        # specific to python PQ
        # the first value of the tuple is treated as the priority value
        if G[start_vertex][adj_vertex] != 0:  # is connected
            priority_queue.put((G[start_vertex][adj_vertex], adj_vertex))

    while not priority_queue.empty():
        # Last vertex in tree and the new minimum
        min_edge = (curr_tree[len(curr_tree) - 1],
                    priority_queue.get()[1])

        if min_edge[1] not in curr_tree:
            curr_tree.append(min_edge[1])
            for adj_vertex in range(len(G[min_edge[1]])):
                if G[min_edge[1]][adj_vertex] != 0:
                    priority_queue.put(
                        (G[min_edge[1]][adj_vertex], adj_vertex))

    return curr_tree


if __name__ == '__main__':
    # print(PrimsMST(SAMPLE_WEIGHTED_UNDIRECTED_GRAPH))
    print(PrimsMST2(SAMPLE_WEIGHTED_UNDIRECTED_GRAPH))
