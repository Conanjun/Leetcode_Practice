#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_198

'''
	House Robber   
	
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


class Solution(object):
	# ***********************************************************************************************************************
	# 思路:动态规划
	# dp递归公式: dp[i]=max(num[i]+dp[i-1],dp[i-1])
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0: return 0
		if len(nums) == 1: return nums[0]

		dp = [0] * len(nums)
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in range(2, len(nums)):
			dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
		return dp[-1]


import unittest


class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution(self):
		solution = Solution()
		nums = [3, 2, 1, 5]
		self.assertTrue(solution.rob(nums) == 8)

		nums = [1, 1, 2, 1]
		self.assertTrue(solution.rob(nums) == 3)


if __name__ == "__main__":
	unittest.main()
