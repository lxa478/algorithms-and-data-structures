#!/usr/bin/python

def word_break(s, words):
	memo = [True] + [False] * len(s)
			
	for i in range(len(s)):
		for j in range(i+1, len(s)):
			if memo[i]==True and s[i:j+1] in words:
				memo[j+1] = True
	
	return memo[-1]
	
print word_break("whatup", {"what", "up"})