from example_unweighted_graphs import UNDIRECTED_1

STATUS = {}
DISCOVER_TIME = {}
FINISH_TIME = {}

NEW = 1
ACTIVE = 2
FINISHED = 3

Vertex = str


def DepthFirstSearch(G: dict[str, list[str]]):
    # force pass by reference
    time = [0]
    for vertex in G.keys():
        STATUS[vertex] = NEW

    for vertex in G.keys():
        if STATUS[vertex] == NEW:
            DFS_visit(G, vertex, time)


def DFS_visit(G: dict[str, list[str]], start: Vertex, time: list[int]):
    '''
    Preprocessing
    '''
    STATUS[start] = ACTIVE
    time[0] += 1
    DISCOVER_TIME[start] = time[0]
    print(f'Discovered vertex {start} at time = {time[0]}')

    '''
    The definition of 'adjacent' could be differnt depending on the graph
    some graphs don't explicitly state what adjacent vertices are
    '''
    for adjacent_vertex in G[start]:
        if STATUS[adjacent_vertex] == NEW:
            DFS_visit(G, adjacent_vertex, time)

    '''
    Postprocessing
    '''
    STATUS[start] = FINISHED
    time[0] += 1
    FINISH_TIME[start] = time[0]
    print(f'=> Finished vertex {start} at time = {time[0]}')


if __name__ == '__main__':
    DepthFirstSearch(UNDIRECTED_1)
    print(DISCOVER_TIME)
    print(FINISH_TIME)
