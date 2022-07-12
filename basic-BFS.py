from queue import Queue
from enum import Enum
from example_unweighted_graphs import UNDIRECTED_3


class STATUS(Enum):
    NEW = 1
    ACTIVE = 2
    FINISHED = 3


def BreadthFirstSearch(G: dict, start_vertex: str):
    VISIT_STATUS: dict[str, STATUS] = {}

    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NEW

    queue = Queue()
    queue.put(start_vertex)

    while not queue.empty():
        first_vertex_in_queue = queue.get()

        if VISIT_STATUS[first_vertex_in_queue] == STATUS.NEW:
            print(f'Discovered: {first_vertex_in_queue}')
            VISIT_STATUS[first_vertex_in_queue] = STATUS.ACTIVE

            for adjacent_vertex in G[first_vertex_in_queue]:
                queue.put(adjacent_vertex)


def BFS_WithToken(G: dict, start_vertex: str):
    TOKEN = '\033[93m*Special Token*\033[0m'
    VISIT_STATUS: dict[str, STATUS] = {}

    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NEW

    queue = Queue()
    queue.put(start_vertex)
    queue.put(TOKEN)

    while not queue.empty():
        first_vertex_in_queue = queue.get()

        if first_vertex_in_queue == TOKEN:
            print(TOKEN)
            if queue.empty():  # If no more vertices, token was the only thing
                break
            else:
                queue.put(TOKEN)
        else:
            if VISIT_STATUS[first_vertex_in_queue] == STATUS.NEW:
                print(f'Discovered: {first_vertex_in_queue}')
                VISIT_STATUS[first_vertex_in_queue] = STATUS.ACTIVE

                for adjacent_vertex in G[first_vertex_in_queue]:
                    queue.put(adjacent_vertex)


if __name__ == '__main__':
    BFS_WithToken(UNDIRECTED_3, 'A')
