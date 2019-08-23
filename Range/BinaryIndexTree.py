class BinaryIndexTree(object):
	def __init__(self, l):
		self.tree = [0] * len(l)
		for i in range(len(l)):
			self.add(i, l[i])
		
	def sum(self, k):
		s = 0
		k += 1
		while k >= 1:
			s += self.tree[k-1]
			k -= k & (-k)
		return s
		
	def add(self, k, x):
		k += 1
		while k <= len(self.tree):
			self.tree[k-1] += x
			k += k & (-k)
			
lst = [1, 3, 4, 8, 6, 1, 4, 2]
bit = BinaryIndexTree(lst)

# Range sum between 2 and 6
a, b = 2, 6
range_sum = bit.sum(b) - bit.sum(a-1)
print(range_sum)