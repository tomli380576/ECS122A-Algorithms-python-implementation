from queue import PriorityQueue, Queue, LifoQueue
from typing import Union
from example_unweighted_graphs import UNDIRECTED_3

Bag = Union[LifoQueue, Queue, PriorityQueue]
Vertex = str

NEW = 1
ACTIVE = 2
FINISHED = 3

STATUS: dict[Vertex, int] = {}


# Handles disconnected graphs
def WhateverFirstSearch_All(G: dict, bag: Bag):
    for vertex in G.keys():
        STATUS[vertex] = NEW
    for vertex in G:
        if STATUS[vertex] == NEW:
            WFS_Visit(G, vertex, bag)


# Helper for WhateverFirstSearch_All
def WFS_Visit(G: dict, start: Vertex, bag: Bag):
    # no initializing here unlike WhateverFirstSearch_Connected()
    # b/c WhateverFirstSearch_All did it already
    bag.put(start)

    while not bag.empty():
        # Get whatever the 'first' vertex is, depending on the data structure
        vertex = bag.get()
        if STATUS[vertex] == NEW:
            print(f'{vertex}')
            STATUS[vertex] = ACTIVE
            for adjacent_vertex in G[vertex]:
                bag.put(adjacent_vertex)


def WhateverFirstSearch_Connected(G, start: Vertex, bag: Bag):
    '''
    This function by itself assumes all vertices in G can be reached from start_vertex
    Needs a wrapper like WhateverFirstSearch_All() for disconnected graphs
    '''

    for vertex in G:
        # Initialize visit status
        STATUS[vertex] = NEW

    bag.put(start)
    while not bag.empty():
        # Get whatever the 'first' vertex is, 
        # depends on the data structure
        vertex = bag.get()
        if STATUS[vertex] == NEW:
            print(f'Newly Discovered {vertex}')
            STATUS[vertex] = ACTIVE
            for adjacent_vertex in G[vertex]:
                bag.put(adjacent_vertex)


if __name__ == '__main__':
    stack = LifoQueue()
    queue = Queue()
    priority_queue = PriorityQueue()

    print('=> With Stack, Depth First:')
    WhateverFirstSearch_All(UNDIRECTED_3, stack)

    print('=> With Queue, Breadth First:')
    WhateverFirstSearch_All(UNDIRECTED_3, queue)
    '''Needs to be weighted'''
    # print('=> With Priority Queue, Best First:')
    # WhateverFirstSearch_All(UNDIRECTED_3, priority_queue)
