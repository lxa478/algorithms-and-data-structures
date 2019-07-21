def quicksort(alist):
	_quicksort(alist, 0, len(alist)-1)

def _quicksort(alist, first, last):
	if first < last:
		split = partition(alist, first, last)
		_quicksort(alist, first, split-1)
		_quicksort(alist, split+1, last)

def partition(alist, first, last):
	pivot = last
	firsthigh = first

	for i in xrange(first, last+1):
		if alist[i] < alist[pivot]:
			alist[i], alist[firsthigh] = alist[firsthigh], alist[i]
			firsthigh += 1

	alist[pivot], alist[firsthigh] = alist[firsthigh], alist[pivot]

	return firsthigh


alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print alist