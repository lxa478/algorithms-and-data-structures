#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def longest_common_subsequence(s1, s2):
	cols = len(s1) + 1
	rows = len(s2) + 1
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	for i in range(1, rows):
		for j in range(1, cols):
			if s2[i-1] == s1[j-1]:
				memo[i][j] = memo[i-1][j-1] + 1
			else:
				memo[i][j] = max(memo[i-1][j], memo[i][j-1])
				
	print_matrix(memo)
	
	i = rows-1
	j = cols-1
	result = []
	while i > 0:
		if memo[i][j] != memo[i-1][j] and memo[i][j] != memo[i][j-1]:
			result.append(s2[i-1])
			i -= 1
			j -= 1
		elif memo[i][j] == memo[i-1][j]:
			i -= 1
		else:
			j -= 1
			
	return memo[-1][-1], result[::-1]

# Expect: 4, abcf	
print longest_common_subsequence('abcdaf', 'acbcf')