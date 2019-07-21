#!/usr/bin/python

def selections(items, n, path):	
	if not n: 
		print path
	else:
		for i in range(len(items)):
			path.append(items[i])
			selections(items, n-1, path)
			path.pop()

a = list('ABC')
selections(a, 2, [])