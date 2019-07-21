#!/usr/bin/python

def permutations(a, i=0):
	if i == len(a):
		print(a)

	for j in range(i, len(a)):
		a[i], a[j] = a[j], a[i]
		permutations(a, i+1)
		a[i], a[j] = a[j], a[i]
		
def permutations2(a, path):
	if not a:
		print path

	for i in range(len(a)):
		path.append(a.pop(i))
		permutations2(a, path)
		a.insert(i, path.pop())			

# EXTRA: Use Combinations
def printCombinations(alist, k, blist):
	if not k: 
		print blist
	for i in range(len(alist)):
		blist.append(alist.pop(i))
		printCombinations(alist, k-1, blist)
		alist.insert(i, blist.pop())
		
def permutations3(a):
	printCombinations(a, len(a), [])

a = list('123')
print 1
permutations(a)
print 2
permutations2(a, [])
print 3
permutations3(a)