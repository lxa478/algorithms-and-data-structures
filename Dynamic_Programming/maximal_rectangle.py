#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''
	
def maximal_rectangle(matrix):
	
	max_area = 0
	height = [0] * (len(matrix[0])+1)
	
	for row in matrix:
		for i in range(len(row)):
			height[i] = height[i] + 1 if row[i] == 1 else 0
			
		stack = [-1]
		for i in range(len(height)):
			while height[i] < height[stack[-1]]:
				h = height[stack.pop()]
				w = i - stack[-1] - 1
				max_area = max(max_area, h * w)
			stack.append(i)
		
	return max_area
				
			
	
print maximal_rectangle([[1,0,0,1,1,1], [1,0,1,1,0,1], [0,1,1,1,1,1], [0,0,1,1,1,1]])