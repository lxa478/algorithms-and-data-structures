#!/usr/bin/python
			
def permutations(a, i=0):
	"""
	All arrangements
	"""
	if i == len(a):
		print(a)

	for j in range(i, len(a)):
		a[i], a[j] = a[j], a[i]
		permutations(a, i+1)
		a[i], a[j] = a[j], a[i]

def combinations(items, k, path):
	"""
	n choose k - unique
	"""
	if not k: 
		print path
	else:	
		for i in range(len(items)):
			path.append(items[i])
			combinations(items[i+1:], k-1, path)
			path.pop()
		
def selections(items, k, path):	
	"""
	n choose k - repetitions
	"""
	if not k: 
		print path
	else:
		for i in range(len(items)):
			path.append(items[i])
			selections(items, k-1, path)
			path.pop()

		
def powerset(a, b):
	"""
	All combinations of size 1 - N
	"""
	print b
	
	for i in range(len(a)):
		b.append(a[i])
		powerset(a[i+1:], b)
		b.pop()