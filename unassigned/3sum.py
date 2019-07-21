#!/usr/bin/python

n = [12, 3, 6, 1, 6, 9]
s = 24

#for i in range(len(n)-1):
#	seen = set()
#	for j in range(i+1, len(n)):
#		target = s - (n[i] + n[j])
#		if target in seen:
#			print n[i], n[j], target
#		else:
#			seen.add(n[j])
#
#print '-'

n.sort()
for i in range(len(n)-1):
	
	l = i + 1
	r = len(n) - 1
	
	while l < r:
		if n[i] + n[l] + n[r] == s:
			print n[l], n[r], n[i]
			l += 1
			r -= 1
		elif n[i] + n[l] + n[r] < s:
			l += 1
		else:
			r -= 1