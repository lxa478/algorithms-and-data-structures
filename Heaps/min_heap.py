#!/usr/bin/python

#MinHeap
#With parent at i, left child is at i*2, and right child is at i*2+1
#A childs at i has a parent at i // 2 (integer division ~ floor)

class MinHeap(object):
	def __init__(self):
		self.heaplist = [0]
		self.currentsize = 0

	def insert(self, k):
		self.heaplist.append(k)
		self.currentsize = self.currentsize + 1
		self.bubble_up(self.currentsize)

	def bubble_up(self, i):
		while i // 2 > 0:
			if self.heaplist[i] < self.heaplist[i // 2]:
				self.heaplist[i // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[i // 2]
			i = i // 2

	def pop_min(self):
		retval = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentsize]
		self.currentsize = self.currentsize - 1
		self.heaplist.pop()
		self.bubble_down(1)
		return retval

	def bubble_down(self, i):
		while (i*2) < self.currentsize:
			mc = self.min_child(i)
			if self.heaplist[i] > self.heaplist[mc]:
				self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
			i = mc

	def min_child(self, i):
		if i * 2 + 1 > self.currentsize:
			return i * 2
		else:
			if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def build_heap(self, alist):
		i = len(alist) // 2
		self.currentsize = len(alist)
		self.heaplist = [0] + alist[:]
		while i > 0:
			self.bubble_down(i)
			i = i - 1


heap = MinHeap()
heap.build_heap([57,52,86,99,32,28,12,44,5,44,30,53,62,3,43,22,19,35,13,79,57,51,50,11,89])
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
heap.insert(3)
heap.insert(5)
print heap.pop_min()
print heap.pop_min()