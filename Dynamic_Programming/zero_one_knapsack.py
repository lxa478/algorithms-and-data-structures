#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def zero_one_knapsack(total, weights, values):
	cols = total + 1
	rows = len(values) + 1
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	for i in range(1, rows):
		for j in range(1, cols):
			if j >= weights[i-1]:
				memo[i][j] = max(memo[i-1][j], memo[i-1][j - weights[i-1]] + values[i-1])
			else:
				memo[i][j] = memo[i-1][j]
	
	print_matrix(memo)

	i = rows-1
	j = cols-1
	result = []
	while i > 0:
		if memo[i][j] != memo[i-1][j]:
			result.append((weights[i-1], values[i-1]))
			j -= weights[i-1]
		else:
			i -= 1
	return memo[-1][-1], result

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print zero_one_knapsack(7, weights, values)