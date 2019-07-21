def mergesort(alist):

	if len(alist) > 1:
		middle = len(alist) // 2
		left = alist[:middle]
		right = alist[middle:]

		mergesort(left)
		mergesort(right)
		merge2(alist, left, right)

def merge2(alist, left, right):
	i = 0

	while left and right:
		if left[0] < right[0]:
			alist[i] = left.pop(0)
		else:
			alist[i] = right.pop(0)
		i += 1

	while left:
		alist[i] = left.pop(0)
		i += 1

	while right:
		alist[i] = right.pop(0)
		i += 1


def merge(alist, left, right):
		i=0
		j=0
		k=0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i = i + 1
			else:
				alist[k] = right[j]
				j = j + 1
			k = k + 1

		while i < len(left):
			alist[k] = left[i]
			i = i + 1
			k = k + 1

		while j < len(right):
			alist[k] = right[j]
			j = j + 1
			k = k + 1

alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print alist