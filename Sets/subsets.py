#!/usr/bin/python

def powerset(a, b):
	print b
	
	for i in range(len(a)):
		b.append(a[i])
		powerset(a[i+1:], b)
		b.pop()
	
def powerset2(a):
	r = [[]]
	for c in a:
		r += ([x+[c] for x in r])
	return r	
	
# EXTRA: Use Combinations
def printUniqueCombinations(alist, numb, blist):
	if not numb: 
		print blist
	for i in range(len(alist)):
		blist.append(alist[i])
		printUniqueCombinations(alist[i+1:], numb-1, blist)
		blist.pop()
		
def powerset3(a):
	for i in range(len(a)+1):
		printUniqueCombinations(a, i, [])
	
a = list('ABC')
powerset(a, [])
print
print powerset2(a)
print
powerset3(a)