def create_adjacency_matrix(edges, num_vertices):
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in edges:
        matrix[u-1][v-1] = matrix[v-1][u-1] = 1
    return matrix

def create_incidence_matrix(edges, num_vertices):
    num_edges = len(edges)
    matrix = [[0] * num_edges for _ in range(num_vertices)]
    for i, (u, v) in enumerate(edges):
        matrix[u-1][i] = matrix[v-1][i] = 1
    return matrix

def find_connected_components(edges, num_vertices):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited, components = set(), []
    def dfs(v, comp):
        visited.add(v)
        comp.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, comp)
    for v in range(1, num_vertices + 1):
        if v not in visited:
            comp = []
            dfs(v, comp)
            components.append(sorted(comp))
    return components
