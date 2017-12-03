#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_1


'''
	Two Sum 
	
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		dict_hash = {}
		for i in range(len(nums)):
			if nums[i] not in dict_hash:
				dict_hash[target - nums[i]] = i  # save the scan result before
			else:
				return [dict_hash[nums[i]], i]


import unittest


class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution(self):
		nums = [2, 7, 11, 15]
		target = 9
		c = Solution()
		self.assertTrue(c.twoSum(nums, target) == [0, 1])


if __name__ == "__main__":
	unittest.main()
