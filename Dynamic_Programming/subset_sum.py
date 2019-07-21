#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def subset_sum(total, nums):
	cols = total + 1
	rows = len(nums) + 1
	
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	for r in range(rows):
		memo[r][0] = 1
			
	for i in range(1, rows):
		for j in range(1, cols):
			if j >= nums[i-1]:
				memo[i][j] = memo[i-1][j] or memo[i-1][j - nums[i-1]]
			else:
				memo[i][j] = memo[i-1][j]
				
	print_matrix(memo)
	
	i = rows-1
	j = cols-1
	result = []
	while i > 0:
		if memo[i][j] != memo[i-1][j]:
			result.append(nums[i-1])
			j -= nums[i-1]
		else:
			i -= 1
	
	return memo[-1][-1], result
	
print subset_sum(11, [2, 3, 7, 8, 10])