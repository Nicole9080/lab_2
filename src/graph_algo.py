 #ГРАФЫ

 def create_adjacency_matrix(edges, num_vertices):
    matrix = []
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            row.append(0)
        matrix.append(row)
  
    for u, v in edges:
        matrix[u-1][v-1] = 1
        matrix[v-1][u-1] = 1
    
    return matrix

def create_incidence_matrix(edges, num_vertices):
    num_edges = len(edges)
    
    matrix = []
    for i in range(num_vertices):
        row = []
        for j in range(num_edges):
            row.append(0)
        matrix.append(row)
    
    for edge_idx, (u, v) in enumerate(edges):
        matrix[u-1][edge_idx] = 1
        matrix[v-1][edge_idx] = 1
    
    return matrix

def find_connected_components(edges, num_vertices):
    graph = {}
    for i in range(1, num_vertices + 1):
        graph[i] = []
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = []
    components = []
    
    def dfs(vertex, component):
        visited.append(vertex)
        component.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for vertex in range(1, num_vertices + 1):
        if vertex not in visited:
            component = []
            dfs(vertex, component)
            components.append(component)
    
    return components

#задание
 num_vertices = 7
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 7)]

print("МАТРИЦА СМЕЖНОСТИ:")
adj_matrix = create_adjacency_matrix(edges, num_vertices)
for row in adj_matrix:
    print(row)

print("\nМАТРИЦА ИНЦИДЕНТНОСТИ:")
inc_matrix = create_incidence_matrix(edges, num_vertices)
for row in inc_matrix:
    print(row)

components = find_connected_components(edges, num_vertices)
print("\nКОМПОНЕНТЫ СВЯЗНОСТИ:", components)
