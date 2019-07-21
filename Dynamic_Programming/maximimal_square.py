#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''
	
def maximimal_square(m):
	cols = len(m[0])
	rows = len(m)
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	for i in range(rows):
		for j in range(cols):
			if m[i][j] == '1':
				memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
	
	print_matrix(memo)
	return max([max(row) for row in memo])
	
	
print maximimal_square(["10100","10111","11111","10010"])