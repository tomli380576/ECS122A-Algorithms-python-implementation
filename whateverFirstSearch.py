from queue import PriorityQueue, Queue, LifoQueue
from typing import Union
from enum import Enum


class STATUS(Enum):
    DISCOVERED = 1
    NOT_DISCOVERED = 2
    FINISHED = 3


# Generic data type that abstracts: put(), get()
Bag = Union[LifoQueue, Queue, PriorityQueue]

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


def WhateverFirstSearch_All(G, data_structure: Bag):
    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NOT_DISCOVERED
    for vertex in G:
        if VISIT_STATUS[vertex] == STATUS.NOT_DISCOVERED:
            WFS_Visit(G, vertex, data_structure)


# Helper for WhateverFirstSearch_All,
# no initializing here unlike WhateverFirstSearch_Connected()
def WFS_Visit(G, start_vertex: str, data_structure: Bag):
    data_structure.put(start_vertex)
    while not data_structure.empty():
        # Get whatever the 'first' vertex is, depending on the data structure
        vertex = data_structure.get()
        if VISIT_STATUS[vertex] == STATUS.NOT_DISCOVERED:
            print(f'Newly Discovered {vertex}')
            VISIT_STATUS[vertex] = STATUS.DISCOVERED
            for adjacent_vertex in G[vertex]:
                data_structure.put(adjacent_vertex)


# This function by itself assumes all vertices in G can be reached from start_vertex
# Needs a wrapper such as WhateverFirstSearch_All() for disconnected graphs
def WhateverFirstSearch_Connected(G, start_vertex: str, data_structure: Bag):
    # Initialize visit status
    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NOT_DISCOVERED

    data_structure.put(start_vertex)
    while not data_structure.empty():
        # Get whatever the 'first' vertex is, depending on the data structure
        vertex = data_structure.get()
        if VISIT_STATUS[vertex] == STATUS.NOT_DISCOVERED:
            print(f'Newly Discovered {vertex}')
            VISIT_STATUS[vertex] = STATUS.DISCOVERED
            for adjacent_vertex in G[vertex]:
                data_structure.put(adjacent_vertex)


if __name__ == '__main__':
    stack = LifoQueue()
    queue = Queue()
    priority_queue = PriorityQueue()

    print('=> With Stack, Depth First:')
    WhateverFirstSearch_All(SAMPLE_UNDIRECTED_GRAPH, stack)

    print('=> With Queue, Breadth First:')
    WhateverFirstSearch_All(SAMPLE_UNDIRECTED_GRAPH, queue)

    print('=> With Priority Queue, Best First:')
    WhateverFirstSearch_All(SAMPLE_UNDIRECTED_GRAPH, priority_queue)
