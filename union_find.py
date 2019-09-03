#!/usr/bin/python
# https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d

class UnionFind:
	def __init__(self, data):
		self.data = data
		
	def union(self, i, j):
		pi, pj = self.find(i), self.find(j)
		if pi != pj:
			self.data[pi] = pj
		
	def find(self, i):
		if i != self.data[i]:
			self.data[i] = self.find(self.data[i])
		return self.data[i]
		
	def connected(i, j):
		return self.find(i) == self.find(j)
		
n = 10
data = [i for i in range(n)]
connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]

uf = UnionFind(data)

for i, j in connections:
	uf.union(i, j)
	
for i in range(n):
	print('item', i, '-> component', uf.find(i))
