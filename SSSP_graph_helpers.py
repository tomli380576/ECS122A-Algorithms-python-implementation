from math import inf
from typing import Union

Vertex = str
Edge = tuple[int, Vertex, Vertex]
WeightedGraph = dict[str, list[tuple[int, str]]]
UnweightedGraph = dict[str, list[str]]
Graph = Union[WeightedGraph, UnweightedGraph]


def GetVertices(G: Graph) -> list[Vertex]:
    return list(G.keys())


def GetWeightedEdges(G: WeightedGraph) -> list[Edge]:
    out: list[Edge] = []
    for vertex, adj_list in G.items():
        for adj_vertex in adj_list:
            out.append((adj_vertex[0], vertex, adj_vertex[1]))
    return out


def InitializeSSSP(G: Graph, start: Vertex) -> tuple[dict, dict]:
    vertices = GetVertices(G)
    assert (start in vertices)

    dist = {vertex: inf for vertex in vertices}
    prev = {vertex: None for vertex in vertices}
    dist[start] = 0

    return dist, prev


def ConstructPath(prev: dict[Vertex, Vertex], end: Vertex) -> list[Vertex]:
    if prev[end] == None:
        return []

    curr = prev[end]
    path = [end]
    '''
    It's like traversing a linked list
    '''
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    '''we appended everything to the back, so reverse it'''
    path.reverse()
    return path
