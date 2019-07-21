#!/usr/bin/python

import heapq 

class PriorityQueue(object):
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0
		
	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))
		
	def pop(self):
		return heapq.heappop(self.elements)[1]

def neighbors(graph, x, y):
	return [(i, j) for i in range(x-1, x+2) 
					for j in range(y-1, y+2)
					if (i != x or j != y) and 
					0 <= i < len(graph) and 
					0 <= j < len(graph[0])]
					
def neighbors2(graph, x, y):
	return [Node(i, j) for i, j in [(x+1, y), (x, y-1), (x-1, y), (x, y+1)] 
	if  0 <= i < len(graph) and  0 <= j < len(graph[0])]
	
def cost(x, y):
	return graph[x][y]
	
def heuristic(a, b):
	# Manhattan Distance
	return abs(a.x - b.x) + abs(a.y - b.y)

class Node(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __hash__(self):
		return hash((self.x, self.y))
		
	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)
		
	def __repr__(self):
		return str("({},{})".format(self.x, self.y))

def dijkstra(graph, start, end):
	''' Shortest path from source vertex to all vertices '''
	priority_queue = PriorityQueue()
	priority_queue.put(start, 0)
	path = {start:None}
	costs = {start:0}
	
	count = 0
	
	while not priority_queue.empty():
		current_node = priority_queue.pop()
		
		if current_node == end:
			break
		
		for next_node in neighbors2(graph, current_node.x, current_node.y):
			new_cost = costs[current_node] + cost(next_node.x, next_node.y)
			if next_node not in costs or new_cost < costs[next_node]:
				costs[next_node] = new_cost
				priority_queue.put(next_node, new_cost)
				path[next_node] = current_node

def floyd_warshall():
	''' Shortest Path from every vertex to all other vertices '''
	pass
	
	
def a_star(graph, start, end):
	''' Shortest Path from start vertex to end verted '''
	priority_queue = PriorityQueue()
	priority_queue.put(start, 0)
	path = {start:None}
	costs = {start:0}
	
	count = 0
	
	while not priority_queue.empty():
		current_node = priority_queue.pop()
		
		if current_node == end:
			# path[end] = current_node
			break
		
		for next_node in neighbors2(graph, current_node.x, current_node.y):
			new_cost = costs[current_node] + cost(next_node.x, next_node.y)
			if next_node not in costs or new_cost < costs[next_node]:
				costs[next_node] = new_cost
				priority_queue.put(next_node, new_cost + heuristic(end, next_node))
				path[next_node] = current_node
		
	current = end
	while current != start:
		print current
		current = path[current]
	print current
	
	
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		 [4, 0, 8, 0, 0, 0, 0, 11, 0],
		 [0, 8, 0, 7, 0, 4, 0, 0, 2],
		 [0, 0, 7, 0, 9, 14, 0, 0, 0],
		 [0, 0, 0, 9, 0, 10, 0, 0, 0],
		 [0, 0, 4, 14, 10, 0, 2, 0, 0],
		 [0, 0, 0, 0, 0, 2, 0, 1, 6],
		 [8, 11, 0, 0, 0, 0, 1, 0, 7],
		 [0, 0, 2, 0, 0, 0, 6, 7, 0]]
		
# print neighbors(graph, 1, 1)
# print neighbors2(graph, 1, 1)

dijkstra(graph, Node(0,0), Node(5,5))
a_star(graph, Node(0,0), Node(5,5))