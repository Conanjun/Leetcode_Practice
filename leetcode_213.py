#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_213

'''
	House Robber II
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


class Solution(object):
	# ***********************************************************************************************************************
	# 思路:动态规划
	# dp递归公式: dp[i]=max(num[i]+dp[i-1],dp[i-1])
	# 这里的关键就是最后那一个房间N和第一个房间相连了，可以这么进行转化：
	# 考虑抢劫了第0个房间，那么问题就是求抢劫第0~N - 1个房间的最大数。
	# 考虑不抢劫第0个房间，那么问题就是求抢劫第1~N个房间的最大数。
	# 上面转化后的两个问题就是HouseRobber I中的问题。再求上面两个解的最大值，就是本题的解。
	def rob(self, nums):
		if len(nums) == 0: return 0
		if len(nums) == 1: return nums[0]
		return max(self.rob_help(nums[:-1]), self.rob_help(nums[1:]))

	def rob_help(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0: return 0
		if len(nums) == 1: return nums[0]

		dp = [0] * len(nums)
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in xrange(2, len(nums)):
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
		self.assertTrue(solution.rob(nums) == 7)

		nums = [1]
		self.assertTrue(solution.rob(nums) == 0)


if __name__ == "__main__":
	unittest.main()
