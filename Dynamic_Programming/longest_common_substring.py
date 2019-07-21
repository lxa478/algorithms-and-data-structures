#!/usr/bin/python

def print_matrix(matrix):
	for i, row in enumerate(matrix):
		print row
	print ''

def longest_common_substring(s1, s2):
	memo = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
	longest = 0
	result = set()
	
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i] == s2[j]:
				if i == 0 or j == 0:
					memo[i][j] = 1
				else:
					memo[i][j] = memo[i-1][j-1] + 1
					
				if memo[i][j] > longest:
					longest = memo[i][j]
					result = set()
					result.add(s1[i-longest+1:i+1])
				elif memo[i][j] == longest:
					result.add(s1[i-longest+1:i+1])
			else:
				memo[i][j] = 0
				
	print_matrix(memo)

	return max([max(x) for x in memo]), result
	
print longest_common_substring('LCLC', 'CLCL')