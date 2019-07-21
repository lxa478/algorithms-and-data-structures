graph = {
    1: [2, 5, 6],
    2: [1, 3, 5],
    3: [2, 4],
    4: [3, 5],
    5: [1, 2, 4],
    6: [1]
}

def process_vertex_early(vertex):
    pass
        
def process_edge(predecessor, successor):
    pass
    
def process_vertex_late(vertex):
    pass

def BFS(graph, start):
    processed = {}
    discovered = {}
    parent = {}
    
    queue = []
    
    queue.append(start)
    discovered[start] = True
    
    while queue:
        vertex = queue.pop(0)
        
        # Process Here
        process_vertex_early(vertex)
        
        processed[vertex] = True
        for edge in graph[vertex]:
            if edge not in processed:
                # Process Here
                process_edge(vertex, edge)
               
            if edge not in discovered:
                queue.append(edge)
                discovered[edge] = True
                parent[edge] = vertex
                
        # Process Here
        process_vertex_late(vertex)
      
    
def DFS(graph, start):
    processed = {}
    discovered = {}
    parent = {}

    paths = []

    stack = []

    stack.append((start, [start]))
    discovered[start] = True

    while stack:
        vertex, path = stack.pop()
        
        # Process Here
        process_vertex_early(vertex)
        
        processed[vertex] = True
        for edge in graph[vertex]:
            if edge not in processed:
                # Process Here
                process_edge(vertex, edge)
               
            if edge not in discovered:
                if edge == 2:
                    print path + [edge]
                else:
                    stack.append((edge, path + [edge]))
                    discovered[edge] = True
                    parent[edge] = vertex
                
        # Process Here
        process_vertex_late(vertex)
  
       
#BFS(graph, 1)
DFS(graph, 1)
