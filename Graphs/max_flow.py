def super_path(entrances, exits, path):
	new_size = len(path[0]) + 2
	new_path = [[0 for _ in range(new_size)] for _ in range(new_size)]
	
	for i in entrances:
		new_path[0][i+1] = float('Inf')
		
	for i in range(len(path)):
		for j in range(len(path[0])):
			new_path[i+1][j+1] = path[i][j]
			
	for i in exits:
		new_path[i+1][new_size-1] = float('Inf')
	
	return 0, new_size-1, new_path
	
def bfs(source, sink, graph, parent):
	visited = [False] * len(graph)
	queue = []
	queue.append(source)
	visited[source] = True
	
	while queue:
		u = queue.pop(0)
		for idx, val in enumerate(graph[u]):
			if visited[idx] == False and val > 0:
				queue.append(idx)
				visited[idx] = True
				parent[idx] = u
	
	return True if visited[sink] else False
	
def ford_fulkerson(source, sink, graph):
	parent = [-1] * len(graph)
	max_flow = 0
	
	while bfs(source, sink, graph, parent):
		path_flow = float('Inf')
		s = sink
		while s != source:
			path_flow = min(path_flow, graph[parent[s]][s])
			s = parent[s]
			
		max_flow += path_flow
		
		v = sink
		while v != source:
			u = parent[v]
			graph[u][v] -= path_flow
			graph[v][u] += path_flow
			v = parent[v]
	
	return max_flow

def answer(entrances, exits, graph):
	source, sink, graph = super_path(entrances, exits, path)
	
	for row in graph:
		print row
	print
	
	return ford_fulkerson(source, sink, graph)
	
entrances = [0, 1]
exits = [4, 5]
path = [
	[0, 0, 4, 6, 0, 0],
	[0, 0, 5, 2, 0, 0],
	[0, 0, 0, 0, 4, 4],
	[0, 0, 0, 0, 6, 6],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
]

print answer(entrances, exits, path)
	
	
			
	
	