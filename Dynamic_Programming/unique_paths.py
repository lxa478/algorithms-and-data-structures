#!/usr/bin/python

def unique_paths(r, c):
	memo = [[1 for _ in range(c)] for _ in range(r)]
	
	for i in range(1, r):
		for j in range(1, c):
			memo[i][j] = memo[i-1][j] + memo[i][j-1]
			
	return memo[-1][-1]	

print unique_paths(3, 7)