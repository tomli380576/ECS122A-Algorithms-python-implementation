from math import inf
from typing import Union, Optional

Vertex = str
WeightedEdge = tuple[int, Vertex, Vertex]
WeightedGraph = dict[str, list[tuple[int, str]]]
UnweightedGraph = dict[str, list[str]]
Graph = Union[WeightedGraph, UnweightedGraph]
Number = Union[
    int, float
]  # this is for handling inf's; Typechecker complains about comparing inf with int


def GetVertices(G: Graph) -> list[Vertex]:
    return list(G.keys())


def GetWeightedEdges(G: WeightedGraph) -> list[WeightedEdge]:
    out: list[WeightedEdge] = []
    for vertex, adj_list in G.items():
        for weight, adj_vertex in adj_list:
            out.append((weight, vertex, adj_vertex))
    return out


def InitializeSSSP(
    G: Graph, start: Vertex
) -> tuple[dict[Vertex, Number], dict[Vertex, Optional[Vertex]]]:
    vertices = GetVertices(G)
    assert start in vertices

    dist = {vertex: inf for vertex in vertices}
    prev = {vertex: None for vertex in vertices}
    dist[start] = 0

    return dist, prev  # type: ignore


def ConstructPath(prev: dict[Vertex, Optional[Vertex]], end: Vertex) -> list[Vertex]:
    if prev[end] == None:
        return []

    curr = prev[end]
    path = [end]
    """
    It's like traversing a linked list
    """
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    """we appended everything to the back, so reverse it"""
    path.reverse()
    return path
