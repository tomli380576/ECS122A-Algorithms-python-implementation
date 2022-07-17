from enum import Enum
from example_unweighted_graphs import UNDIRECTED_1

VISIT_STATUS = {}
DISCOVER_TIME = {}
FINISH_TIME = {}


class STATUS(Enum):
    NEW = 1
    ACTIVE = 2
    FINISHED = 3


def DepthFirstSearch(G: dict[str, list[str]]):
    # force pass by reference
    time = [0]
    for vertex in G.keys():
        VISIT_STATUS[vertex] = STATUS.NEW

    for vertex in G.keys():
        if VISIT_STATUS[vertex] == STATUS.NEW:
            DFS_visit(G, vertex, time)


def DFS_visit(G: dict[str, list[str]], start_vertex: str, time: list[int]):
    VISIT_STATUS[start_vertex] = STATUS.ACTIVE
    time[0] += 1
    DISCOVER_TIME[start_vertex] = time[0]
    print(f'Discovered vertex {start_vertex} at time = {time[0]}')

    for adjacent_vertex in G[start_vertex]:  # Adjacent vertices
        if VISIT_STATUS[adjacent_vertex] == STATUS.NEW:
            DFS_visit(G, adjacent_vertex, time)

    VISIT_STATUS[start_vertex] = STATUS.FINISHED
    time[0] += 1
    FINISH_TIME[start_vertex] = time[0]
    print(f'=> Finished vertex {start_vertex} at time = {time[0]}')


if __name__ == '__main__':
    DepthFirstSearch(UNDIRECTED_1)
    print(DISCOVER_TIME)
    print(FINISH_TIME)
