#!/usr/bin/python
	
def wildard_matching(s, p):
	"""
	'?' matches any one character
	"*" matches 0 or more of any character
	"""
		
	# Filter multiple stars
	new_p = []
	prev = ''
	for c in p:
		if not (prev == '*' and c == '*'):
			new_p.append(c)
		prev = c
	p = new_p
			
	cols = len(p)+1
	rows = len(s)+1
	memo = [[False for _ in range(cols)] for _ in range(rows)]
		
	memo[0][0] = True
	memo[0][1] = p[0] == '*'	
			
	for i in range(1, rows):
		for j in range(1, cols):
			
			if s[i-1] == p[j-1] or p[j-1] == '?':
				memo[i][j] = memo[i-1][j-1]
			elif p[j-1] == '*':
				memo[i][j] = memo[i-1][j] or memo[i][j-1]
				
	print_matrix(memo)
	return memo[-1][-1] 
	
print wildard_matching("ho", "**ho")