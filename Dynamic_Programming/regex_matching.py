#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def regex_matching(s, p):
	"""
	'.' matches any one character
	"*" matches 0 or more of the previous character
	"""
	
	cols = len(p)+1
	rows = len(s)+1
	memo = [[False for _ in range(cols)] for _ in range(rows)]
	memo[0][0] = True
	
	for i in range(1, cols):
		if p[i-1] == '*':
			memo[0][i] = memo[0][i-2]
		
	for i in range(1, rows):
		for j in range(1, cols):
			if s[i-1] == p[j-1] or p[j-1] == '.':
				memo[i][j] = memo[i-1][j-1]
			elif p[j-1] == '*':
				if s[i-1] == p[j-2] or p[j-2] == '.':
					memo[i][j] = memo[i][j-2] or memo[i-1][j]
				else:
					memo[i][j] = memo[i][j-2]
	
	print_matrix(memo)			
	return memo[-1][-1]
	
print regex_matching('abcd', 'a*bc.')
