from example_unweighted_graphs import DIRECTED_CYCLIC_1, DIRECTED_CYCLIC_2

STATUS = {}
DISCOVER_TIME = {}
FINISH_TIME = {}

NEW = 1
ACTIVE = 2
FINISHED = 3

Vertex = str


def ClassifyEdge(prev, curr):
    if prev != None:
        stat_prev = STATUS[prev]
        stat_curr = STATUS[curr]
        if stat_prev == ACTIVE and stat_curr == NEW:
            print(f'\033[92mTree\033[0m: {prev} -> {curr}')
        elif stat_prev == ACTIVE and stat_curr == ACTIVE:
            print(f'\033[91mBack\033[0m: {prev} -> {curr}')
        elif stat_prev == FINISHED and stat_curr == ACTIVE:
            print(f'Forward or cross: {prev} -> {curr}')


def DFS_CycleDetection(G: dict[str, list[str]]):
    # force pass by reference
    time = [0]
    for vertex in G.keys():
        STATUS[vertex] = NEW

    for vertex in G.keys():
        if STATUS[vertex] == NEW:
            DFS_visit(G, vertex, time)


def DFS_visit(G: dict[str, list[str]], curr: Vertex, time: list[int]):
    '''
    Preprocessing
    '''
    STATUS[curr] = ACTIVE
    time[0] += 1
    DISCOVER_TIME[curr] = time[0]
    '''
    The definition of 'adjacent' could be differnt depending on the graph
    some graphs don't explicitly state what adjacent vertices are
    '''
    for adjacent_vertex in G[curr]:
        ClassifyEdge(curr, adjacent_vertex)
        if STATUS[adjacent_vertex] == NEW:
            DFS_visit(G, adjacent_vertex, time)
    '''
    Postprocessing
    '''
    STATUS[curr] = FINISHED
    time[0] += 1
    FINISH_TIME[curr] = time[0]


if __name__ == '__main__':
    print('===> Traversing: DIRECTED_CYCLIC_1')
    DFS_CycleDetection(DIRECTED_CYCLIC_1)
    print('===> Traversing: DIRECTED_CYCLIC_2')
    DFS_CycleDetection(DIRECTED_CYCLIC_2)
