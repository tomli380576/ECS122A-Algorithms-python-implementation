from example_unweighted_graphs import UNDIRECTED_1

VISIT_STATUS = {}
DISCOVER_TIME = {}
FINISH_TIME = {}


def DFS_search(G: dict[str, list[str]]):
    # force pass by reference, technically bad cuz it's a global mutable
    time = [0]
    for vertex in G.keys():
        VISIT_STATUS[vertex] = 'undiscovered'

    for vertex in G.keys():
        if VISIT_STATUS[vertex] == 'undiscovered':
            DFS_visit(G, vertex, time)


def DFS_visit(G: dict[str, list[str]], start_vertex: str, time: list[int]):
    print(f'Discovered vertex {start_vertex} at time = {time[0]}')

    VISIT_STATUS[start_vertex] = 'discovered'
    time[0] += 1

    for adjacent_vertex in G[start_vertex]:  # Adjacent vertices
        if VISIT_STATUS[adjacent_vertex] == 'undiscovered':
            DFS_visit(G, adjacent_vertex, time)

    VISIT_STATUS[start_vertex] = 'finished'
    time[0] += 1
    FINISH_TIME[start_vertex] = time[0]

    print(f'=> Finish vertex {start_vertex} at time = {time[0]}')


if __name__ == '__main__':
    DFS_search(UNDIRECTED_1)
