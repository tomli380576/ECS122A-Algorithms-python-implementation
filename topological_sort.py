from example_unweighted_graphs import DIRECTED_ACYCLIC_2, DIRECTED_ACYCLIC_1
from enum import Enum


class STATUS(Enum):
    ACTIVE = 1
    NEW = 2
    FINISHED = 3


VISIT_STATUS = {}
ORDER = {}


def TopologicalSort(G: dict[str, list[str]]):
    VISIT_STATUS.clear()
    ORDER.clear()
    for vertex in G:
        VISIT_STATUS[vertex] = STATUS.NEW

    clock = len(G.keys())

    for vertex in G:
        if VISIT_STATUS[vertex] == STATUS.NEW:
            clock = TopologicalVisit(G, vertex, clock)
    return ORDER


def TopologicalVisit(G: dict[str, list[str]], vertex: str, clock: int) -> int:
    VISIT_STATUS[vertex] = STATUS.ACTIVE

    for adjacent_vertex in G[vertex]:
        if VISIT_STATUS[adjacent_vertex] == STATUS.NEW:
            clock = TopologicalVisit(G, adjacent_vertex, clock)
        elif VISIT_STATUS[adjacent_vertex] == STATUS.ACTIVE:
            raise RuntimeError('Cycle Detected')

    VISIT_STATUS[vertex] = STATUS.FINISHED
    ORDER[vertex] = clock
    clock -= 1
    return clock


if __name__ == '__main__':
    result1 = TopologicalSort(DIRECTED_ACYCLIC_1)
    sorted_dict1 = {
        k: v
        for k, v in sorted(result1.items(), key=lambda item: item[1])
    }

    result2 = TopologicalSort(DIRECTED_ACYCLIC_2)
    sorted_dict2 = {
        k: v
        for k, v in sorted(result2.items(), key=lambda item: item[1])
    }

    print(
        f'{list(sorted_dict1.keys())} is 1 way of topologically sorting DIRECTED_ACYCLIC_1'
    )
    print(
        f'{list(sorted_dict2.keys())} is 1 way of topologically sorting DIRECTED_ACYCLIC_2'
    )
