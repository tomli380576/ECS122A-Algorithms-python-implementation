from queue import Queue
from math import inf

Graph = dict[str, list[tuple[int, str]]]


def GetVertices(G: Graph) -> list[str]:
    return list(G.keys())


def InitializeSSSP(G: Graph, start_vertex: str) -> tuple[dict, dict]:
    vertices = GetVertices(G)
    assert (start_vertex in vertices)

    dist = {vertex: inf for vertex in vertices}
    prev = {vertex: None for vertex in vertices}
    dist[start_vertex] = 0

    return dist, prev


def mooresSSSP(G, start_vertex):
    dist, prev = InitializeSSSP(G, start_vertex)

    pass
