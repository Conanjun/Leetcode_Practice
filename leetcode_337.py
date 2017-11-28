#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_337

from utils.BinaryTree import TreeNode

'''
	House Robber III
	
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police. 

Example 1:

     3
    / \
   2   3
    \   \ 
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7. 

Example 2:

     3
    / \
   4   5
  / \   \ 
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9. 

'''


# ***********************************************************************************************************************
class Solution(object):
	'''
	思路:
	Let
	f1(node) be the value of maximum money we can rob from the subtree with node as root ( we can rob node if necessary).
	f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.
	Then we have
	f2(node) = f1(node.left) + f1(node.right) and
	f1(node) = max( f2(node.left)+f2(node.right)+node.value, f2(node) ).
	'''

	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return self.robDFS(root)[1]

	def robDFS(self, node):
		if node is None:
			return (0, 0)  # (f2(node),f1(node))
		l = self.robDFS(node.left)
		r = self.robDFS(node.right)
		# f2(node) without node
		# f1(node) with node
		return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))


import unittest


class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution(self):
		solution = Solution()
		'''
			 3
			/ \
		   2   3
			\   \ 
			 3   1
		'''
		node1 = TreeNode(3)
		node2 = TreeNode(2)
		node3 = TreeNode(3)
		node4 = TreeNode(3)
		node5 = TreeNode(1)
		node1.left = node2
		node1.right = node3
		node2.right = node4
		node3.right = node5
		self.assertTrue(solution.rob(node1) == 7)

		'''
			 3
			/ \
		   4   5
		  / \   \ 
		 1   3   1
		'''
		node1 = TreeNode(3)
		node2 = TreeNode(4)
		node3 = TreeNode(5)
		node4 = TreeNode(1)
		node5 = TreeNode(3)
		node6 = TreeNode(1)
		node1.left = node2
		node1.right = node3
		node2.left = node4
		node2.right = node5
		node3.right = node6
		self.assertTrue(solution.rob(node1) == 9)


if __name__ == "__main__":
	unittest.main()
