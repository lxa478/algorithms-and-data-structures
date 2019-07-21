#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def rod_cutting(size, prices):
	cols = size + 1
	rows = len(prices)+1
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
		
	for i in range(1, rows):
		for j in range(1, cols):
			if j >= i:
				memo[i][j] = max(memo[i-1][j], memo[i][j - i] + prices[i-1])
			else:
				memo[i][j] = memo[i-1][j]
	
	print_matrix(memo)
	
	i = rows-1
	j = cols-1
	result = []
	while i > 0:
		if memo[i][j] != memo[i-1][j]:
			result.append(i)
			j -= i
		else:
			i -= 1
			
	return memo[-1][-1], result
		
print rod_cutting(5, [2, 5, 7, 8])