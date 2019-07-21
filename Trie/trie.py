#!/usr/bin/python

class Trie(object):
	def __init__(self):
		self.root = {}

	def insert(self, word):
		node = self.root
		for c in word:
			if c not in node:
				node[c] = {}
			node = node[c]
		node['#'] = '#'
		

	def search(self, word, is_word=True):
		node = self.root
		for c in word:
			if c not in node:
				return False
			node = node[c]
			
		return '#' in node if is_word else True
		

	def startsWith(self, prefix):
		return self.search(prefix, False)
