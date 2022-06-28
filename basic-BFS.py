from queue import PriorityQueue, Queue, LifoQueue
from typing import Union
from enum import Enum


class STATUS(Enum):
    DISCOVERED = 1
    NOT_DISCOVERED = 2
    FINISHED = 3


VISIT_STATUS: dict[str, STATUS] = {}
SAMPLE_DIRECTED_GRAPH: dict[str, list[str]] = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
SAMPLE_UNDIRECTED_GRAPH: dict[str, list[str]] = {
    '5': ['3', '7'],
    '3': ['2', '4', '5'],
    '7': ['8', '5'],
    '2': ['3'],
    '4': ['8', '3'],
    '8': ['4', '7']
}
SAMPLE_UNDIRECTED_GRAPH2: dict[str, list[str]] = {
    'A': ['B', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'E': ['A', 'C'],
    'D': ['B', 'C']
}


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


if __name__ == '__main__':
    BreadthFirstSearch(SAMPLE_UNDIRECTED_GRAPH2, 'A')
