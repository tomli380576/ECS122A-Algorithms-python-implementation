from queue import Queue
from enum import Enum
from example_unweighted_graphs import UNDIRECTED_3


class STATUS(Enum):
    DISCOVERED = 1
    NOT_DISCOVERED = 2
    FINISHED = 3


VISIT_STATUS: dict[str, STATUS] = {}


def BreadthFirstSearch(G: dict, start_vertex: str):
    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NOT_DISCOVERED

    queue = Queue()
    queue.put(start_vertex)
    while not queue.empty():
        first_vertex_in_queue = queue.get()
        if VISIT_STATUS[first_vertex_in_queue] == STATUS.NOT_DISCOVERED:
            print(f'Discovered: {first_vertex_in_queue}')
            VISIT_STATUS[first_vertex_in_queue] = STATUS.DISCOVERED
            for adjacent_vertex in G[first_vertex_in_queue]:
                queue.put(adjacent_vertex)


def BFS_WithToken(G: dict, start_vertex: str):
    TOKEN = '\033[96m*Special Token*\033[0m'

    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NOT_DISCOVERED

    queue = Queue()
    queue.put(start_vertex)
    queue.put(TOKEN)
    while not queue.empty():
        first_vertex_in_queue = queue.get()
        if first_vertex_in_queue == TOKEN:
            print(TOKEN)
            if queue.empty():  # If token was the last thing in queue
                break
            else:
                queue.put(TOKEN)
        else:
            if VISIT_STATUS[first_vertex_in_queue] == STATUS.NOT_DISCOVERED:
                print(f'Discovered: {first_vertex_in_queue}')
                VISIT_STATUS[first_vertex_in_queue] = STATUS.DISCOVERED
                for adjacent_vertex in G[first_vertex_in_queue]:
                    queue.put(adjacent_vertex)


if __name__ == '__main__':
    BFS_WithToken(UNDIRECTED_3, 'A')
