#!/usr/bin/python
from collections import deque	
			
def bfs(graph, start):
	''' Breadth First Search '''
	queue = deque(start)
	path = {start:None}
	
	while queue:
		current_node = queue.popleft()
		for next_node in graph[current_node]:
			if next_node not in path:
				queue.append(next_node)
				path[next_node] = current_node
	print path			
				
def dfs(graph, start):
	''' Depth First Search '''
	stack = deque(start)
	path = {start:None}
	
	while stack:
		current_node = stack.pop()
		for next_node in graph[current_node]:
			if next_node not in path:
				stack.append(next_node)
				path[next_node] = current_node
	print path
							
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

bfs(graph, 'A')
dfs(graph, 'A')