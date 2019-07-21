def binary_search(alist, item):
	
	low = 0
	high = len(alist) - 1
	
	while low <= high:
		mid = (low + high) // 2
				
		if alist[mid] == item:
			return True
		
		if item < alist[mid]:
			high = mid - 1
		else:
			low = mid + 1
			
	return False


alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
print binary_search(alist, 42)
print binary_search(alist, 44)