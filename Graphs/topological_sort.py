#!/usr/bin/python

"""
See: https://github.com/harishvc/challenges/blob/master/graph-detect-cycle-topological-sort.py
for DFS with cycle detection
"""

def topological_sort(graph):
	''' Topological Sort '''
	
	def dfs(graph, vertex, visited, resp):		
		visited.add(vertex)
		
		for edge in graph[vertex]:
			if edge not in visited:
				dfs(graph, edge, visited, resp)
		
		resp.append(vertex)
		
		
	visited = set()
	resp = []
	
	for edge in graph:
		if edge not in visited:
			dfs(graph, edge, visited, resp)
			
	return resp
	
	
	
def topo_sort_2(n, pairs):
	order = [0 for i in range(n)]
	graph = {n:[] for n in range(n)}
	for pair in pairs:
		graph[pair[1]].append(pair[0])
		order[pair[0]] += 1
	
	sorted_stack = []
	zero_stack = [i for i in range(len(order)) if order[i]==0]
			
	while zero_stack:
		vertex = zero_stack.pop()
		
		for edge in graph[vertex]:
			order[edge] -= 1
			if order[edge] == 0:
				zero_stack.append(edge)
				
		sorted_stack.append(vertex)
		
	return sorted_stack if len(sorted_stack) == len(order) else []
	

print topo_sort_2(4, [[1,0],[2,1],[3,2],[1,3]])
	

	
'''
	 +---- A
	 |   /   \
	 |  B--D--C
	 |   \ | /
	 +---- E
'''

graph = {
	'A': ['B','C'], 
	'B': ['D','E'], 
	'C': ['D','E'], 
	'D': ['E'], 
	'E': ['A']}

print topological_sort(graph)