from queue import PriorityQueue, Queue, LifoQueue
from typing import Union
from enum import Enum
from example_unweighted_graphs import UNDIRECTED_3


class STATUS(Enum):
    DISCOVERED = 1
    NOT_DISCOVERED = 2
    FINISHED = 3


# Generic data type that has: put(), get(), empty()
Bag = Union[LifoQueue, Queue, PriorityQueue]

VISIT_STATUS: dict[str, STATUS] = {}


# Handles disconnected graphs
def WhateverFirstSearch_All(G, data_structure: Bag):
    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NOT_DISCOVERED
    for vertex in G:
        if VISIT_STATUS[vertex] == STATUS.NOT_DISCOVERED:
            WFS_Visit(G, vertex, data_structure)


# Helper for WhateverFirstSearch_All
def WFS_Visit(G, start_vertex: str, data_structure: Bag):
    # no initializing here unlike WhateverFirstSearch_Connected()
    # b/c WhateverFirstSearch_All did it already
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
    WhateverFirstSearch_All(UNDIRECTED_3, stack)

    print('=> With Queue, Breadth First:')
    WhateverFirstSearch_All(UNDIRECTED_3, queue)

    print('=> With Priority Queue, Best First:')
    WhateverFirstSearch_All(UNDIRECTED_3, priority_queue)
