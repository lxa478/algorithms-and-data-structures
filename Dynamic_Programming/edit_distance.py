#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''
	
def edit_distance(s1, s2):
	cols = len(s1) + 1
	rows = len(s2) + 1
	memo = [[0 for _ in range(cols)] for _ in range(rows)]
	
	for i in range(1, rows):
		memo[i][0] = memo[i-1][0] + 1
		
	for i in range(1, cols):
		memo[0][i] = memo[0][i-1] + 1
	
	for i in range(1, rows):
		for j in range(1, cols):
			if s1[j-1] != s2[i-1]:
				memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
			else:
				memo[i][j] = memo[i-1][j-1]
				
	i = rows-1
	j = cols-1
	result = []
	
	while i > 0:
		if s1[j-1] == s2[i-1]:
			i -= 1
			j -= 1
		else:
			if memo[i-1][j] < memo[i][j-1] and memo[i-1][j] < memo[i-1][j-1]:
				result.append("Add %c" % s2[i-1])
				i -= 1
			elif memo[i][j-1] < memo[i-1][j] and memo[i][j-1] < memo[i-1][j-1]:
				result.append("Delete %c" % s1[j-1])
				j -= 1
			else:
				result.append("Edit %c to %c" % (s1[j-1], s2[i-1]))
				i -= 1
				j -= 1
	
	print_matrix(memo)
	return memo[-1][-1], result[::-1]
	
print edit_distance('abcdef', 'azced')