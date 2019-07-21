#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

# 2D
def coin_change_num_ways(total, coins):
	cols = total + 1
	rows = len(coins) + 1
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	for r in range(rows):
		memo[r][0] = 1
	
	for i in range(1, rows):
		for j in range(1, cols):
			if j >= coins[i-1]:
				memo[i][j] = memo[i-1][j] + memo[i][j - coins[i-1]]
			else:
				memo[i][j] = memo[i-1][j]
				
	print_matrix(memo)
	return memo[-1][-1]
	
print coin_change_num_ways(5, [1, 2, 5])

# 1D
def coin_change_num_ways2(total, coins):
	amounts = [1] + [0] * total	
	for coin in coins:
		for i in range(coin, total+1):
			amounts[i] += amounts[i - coin]
				
	return amounts[-1]

print coin_change_num_ways2(5, [1, 2, 5])