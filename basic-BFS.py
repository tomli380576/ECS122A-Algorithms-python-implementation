from queue import Queue
from example_unweighted_graphs import UNDIRECTED_3
from graph_helpers import UnweightedGraph

NEW = 1
VISITED = 2
Vertex = str


# I know it says unweighted here
# but any graph should work
def BreadthFirstSearch(G: UnweightedGraph, start: Vertex):
    STATUS: dict[Vertex, int] = {}

    for vertex in G:
        STATUS[vertex] = NEW

    queue = Queue()
    queue.put(start)

    while not queue.empty():
        first_vertex = queue.get()

        if STATUS[first_vertex] == NEW:
            print(f'{first_vertex}')
            STATUS[first_vertex] = VISITED
            for adjacent_vertex in G[first_vertex]:
                queue.put(adjacent_vertex)


def BFS_122A_Version(G: UnweightedGraph, start: Vertex):
    STATUS: dict[Vertex, int] = {}

    for vertex in G:
        STATUS[vertex] = NEW

    queue = Queue()
    queue.put(start)
    STATUS[start] = VISITED

    while not queue.empty():
        first_vertex = queue.get()
        print(first_vertex)
        for adjacent_vertex in G[first_vertex]:
            if STATUS[adjacent_vertex] == NEW:
                STATUS[adjacent_vertex] = VISITED
                queue.put(adjacent_vertex)


def BFS_WithToken(G: UnweightedGraph, start: Vertex):
    TOKEN = '\033[93m*Special Token*\033[0m'
    STATUS: dict[str, int] = {}

    for vertex in G:
        STATUS[vertex] = NEW

    queue = Queue()
    queue.put(start)
    queue.put(TOKEN)

    while not queue.empty():
        first_vertex = queue.get()
        if first_vertex == TOKEN:
            print(TOKEN)
            ''' 
            If no more vertices, token is the only thing
            '''
            if queue.empty():
                break
            else:
                queue.put(TOKEN)
        else:
            if STATUS[first_vertex] == NEW:
                print(f'{first_vertex}')
                STATUS[first_vertex] = VISITED

                for adjacent_vertex in G[first_vertex]:
                    queue.put(adjacent_vertex)


if __name__ == '__main__':
    print('==> Whatever-First based version:')
    show_token = True
    if show_token:
        BFS_WithToken(UNDIRECTED_3, 'S')
    else:
        BreadthFirstSearch(UNDIRECTED_3, 'S')
    print('\n==> 122A version')
    BFS_122A_Version(UNDIRECTED_3, 'S')
