#!/usr/bin/python

def longest_increasing_subsequence(nums):
	memo = [1] * len(nums)
	idx = [0] * len(nums)
	
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[j] > nums[i]:
				memo[j] = max(memo[j], memo[i]+1)

	return max(memo)
	
print longest_increasing_subsequence([3,4,-1,0,6,2,3])