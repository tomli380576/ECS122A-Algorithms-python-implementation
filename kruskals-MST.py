import numpy as np

SAMPLE_WEIGHTED_UNDIRECTED_GRAPH = np.array([[0, 9, 75, 0, 0],
                                             [9, 0, 95, 19, 42],
                                             [75, 95, 0, 51, 66],
                                             [0, 19, 51, 0, 31],
                                             [0, 42, 66, 31, 0]])


def getEdges(G: np.ndarray):
    num_vertices = len(G)
    edges = []
    for y in range(num_vertices):
        for x in range(num_vertices):
            if x < y and G[y, x] != 0:
                edges.append((y, x))
    return edges


def find(u, v, all_sets: list[set]):
    set_with_u = -1
    set_with_v = -1

    for idx, _set in enumerate(all_sets):
        if u in _set:
            set_with_u = idx
        if v in _set:
            set_with_v = idx
    if set_with_u == -1 or set_with_v == -1:
        raise ValueError('No sets found containing u or v')
    else:
        return set_with_u, set_with_v


def KruskalsMST(G):
    # Edges are stored as (y, x), sort by the weight G[y, x]
    sorted_edges = sorted(getEdges(G), key=lambda edge: G[edge])
    curr_tree: list[tuple] = []
    sets: list[set] = []

    # make_set(v)
    for vertex in range(len(G)):
        sets.append(set([vertex]))

    for edge in sorted_edges:
        u, v = edge
        set_with_u_idx, set_with_v_idx = find(u, v,
                                              all_sets=sets)  # returns index
        if set_with_u_idx != set_with_v_idx:  # if find(u, v)
            # Simulates union(u, v)
            # merge in to set v first, then remove set u
            # avoids ambiguous index shifting
            sets[set_with_v_idx] = sets[set_with_v_idx].union(
                sets[set_with_u_idx])
            sets.pop(set_with_u_idx)
            curr_tree.append(edge)
    return curr_tree


if __name__ == '__main__':
    print(
        f'Edges selected by Kruskal\'s MST: {KruskalsMST(SAMPLE_WEIGHTED_UNDIRECTED_GRAPH)}'
    )
