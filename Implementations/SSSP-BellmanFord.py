from example_weighted_graphs import W_DIRECTED_1, W_DIRECTED_2
from graph_helpers import (
    InitializeSSSP,
    GetVertices,
    GetWeightedEdges,
    ConstructPath,
    Vertex,
    WeightedGraph,
)
import random


def BellmanFord(G: WeightedGraph, start: Vertex):
    dist, prev = InitializeSSSP(G, start)
    num_vertices = len(GetVertices(G))
    edges = GetWeightedEdges(G)
    """
    Underscore means we don't use this variable
    """
    for _ in range(num_vertices - 1):
        for edge in edges:
            weight, u, v = edge
            """
            If tense, relax it
            """
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
    """
    Now there shouldn't be any tense edges,
    If we find any, then the graph has a negative cycle
    """
    for edge in edges:
        weight, u, v = edge
        if dist[u] + weight < dist[v]:
            raise ValueError("Negative Cycle, No solution")

    print("No Cycles Found")

    return dist, prev


if __name__ == "__main__":
    run_on_all_vertices = False
    graph = W_DIRECTED_1

    if run_on_all_vertices:
        for start in GetVertices(graph):
            # start = '3'
            dist, prev = BellmanFord(graph, start)
            for end in GetVertices(graph):
                if end != start:
                    path = ConstructPath(prev, end)
                    if len(path) > 0:
                        print(f"Shortest Path from {start} to {end} is {path}")
                    else:
                        print(f"\033[91mNo path from '{start}' to '{end}'\033[0m")
            print("=============")
    else:
        start = random.choice(GetVertices(graph))
        print(f"==> Selected start: {start}")
        dist, prev = BellmanFord(graph, start)
        for end in GetVertices(graph):
            if end != start:
                path = ConstructPath(prev, end)
                if len(path) > 0:
                    print(f"Shortest Path from {start} to {end} is {path}")
                else:
                    print(f"\033[91mNo path from '{start}' to '{end}'\033[0m")
