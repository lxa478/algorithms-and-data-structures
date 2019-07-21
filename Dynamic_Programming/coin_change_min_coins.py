#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def coin_change_min_coins(total, coins):
	cols = total + 1
	rows = len(coins) + 1
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	memo[0] = [float("inf")] * cols
	memo[0][0] = 0
	
	for i in range(1, rows):
		for j in range(1, cols):
			if j >= coins[i-1]:
				memo[i][j] = min(memo[i-1][j], memo[i][j - coins[i-1]] + 1)
			else:
				memo[i][j] = memo[i-1][j]
			
	print_matrix(memo)
				
	i = rows-1
	j = cols-1
	result = []
	while i > 0:
		if memo[i][j] != memo[i-1][j]:
			result.append(coins[i-1])
			j -= coins[i-1]
		else:
			i -= 1 
	return memo[-1][-1], result

print coin_change_min_coins(5, [1, 2, 3])