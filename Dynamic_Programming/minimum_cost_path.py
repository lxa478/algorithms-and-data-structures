#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def minimum_cost_path(grid):
	
	cols = len(grid[0])
	rows = len(grid)
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	memo[0][0] = grid[0][0]
	
	
	for i in range(1, rows):
		memo[i][0] = memo[i-1][0] + grid[i][0]
		
	for j in range(1, cols):
		memo[0][j] = memo[0][j-1] + grid[0][j]
		
	for i in range(1, rows):
		for j in range(1, cols):
			memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + grid[i][j]
			
	print_matrix(memo)
	
	i = rows-1
	j = cols-1
	result = []
	while i >= 0 and j >= 0:
		result.append(grid[i][j])
		if memo[i-1][j] < memo[i][j]:
			i -= 1
		else:
			j -= 1
			
	return memo[-1][-1], result[::-1]
	
print minimum_cost_path([[1,3,5,8],[4,2,1,7],[4,3,2,3]])
			
			