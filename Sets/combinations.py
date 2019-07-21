#!/usr/bin/python

def printUniqueCombinations(alist, k, blist):
	if not k: 
		print blist
	else:	
		for i in range(len(alist)):
			blist.append(alist[i])
			printUniqueCombinations(alist[i+1:], k-1, blist)
			blist.pop()

def printCombinations(alist, k, blist):
	if not k: 
		print blist
	else:
		for i in range(len(alist)):
			blist.append(alist.pop(i))
			printCombinations(alist, k-1, blist)
			alist.insert(i, blist.pop())
		
a = list('ABC')
printUniqueCombinations(a, 1, [])
printUniqueCombinations(a, 2, [])
printUniqueCombinations(a, 3, [])
print
printCombinations(a, 1, [])
printCombinations(a, 2, [])
printCombinations(a, 3, [])