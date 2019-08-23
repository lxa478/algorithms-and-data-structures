class SegmentTree(object):
	def __init__(self, lst):
		self.tree = [0] * len(lst) + lst
		for i in reversed(range(1, len(lst))):
			self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
				
	def sum(self, a, b):
		n = len(self.tree)//2
		a += n
		b += n
		s = 0
		while a <= b:
			if a%2 == 1:
				s += self.tree[a]
				a += 1
				
			if b%2 == 0:
				s += self.tree[b]
				b -= 1
			
			a //= 2
			b //= 2
			
		return s
		
	def add(self, k, x):
		k += len(self.tree)//2
		self.tree[k] += x
		while k >= 1:
			k //= 2
			self.tree[k] = self.tree[k<<1] + self.tree[k<<1|1]
		
lst = [5, 8, 6, 3, 2, 7, 2, 6]
st = SegmentTree(lst)
print(st.tree)
print(st.sum(2, 7))