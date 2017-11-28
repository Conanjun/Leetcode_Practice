#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_153

'''
	Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


class Solution(object):
	# ***********************************************************************************************************************
	# 思路:经过处理的二分查找

	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		i = 0
		j = len(nums) - 1
		min_num = nums[0]
		while i < j:
			mid = (i + j) // 2
			if nums[i] <= nums[mid]:
				i = mid + 1
				min_num = min(nums[i], min_num)
			else:
				j = mid - 1
				min_num = min(nums[mid], min_num)
			# else:
			# 	# 左边和中间相等的情况，无法判断哪一边是有序的一边，对边缘移动一步直到不相等
			# 	i = i + 1
			# 	min_num = min(nums[i],min_num)
		return min_num


import unittest


class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution(self):
		solution = Solution()
		nums = [4, 5, 6, 7, 0, 1, 2]
		self.assertTrue(solution.findMin(nums) == 0)

		nums = [6, 7, 0, 1, 2, 4, 5]
		self.assertTrue(solution.findMin(nums) == 0)

		nums = [2,1]
		self.assertTrue(solution.findMin(nums) == 1)


if __name__ == "__main__":
	unittest.main()
