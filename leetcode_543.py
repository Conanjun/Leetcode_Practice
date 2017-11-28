#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_543

from utils.BinaryTree import TreeNode

'''
	Diameter of Binary Tree 
	
  Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]. 

'''


# ***********************************************************************************************************************
class Solution(object):
	'''
	思路:
	递归遍历每个节点，记录当前最大长度(通过某个节点的最大长度为depth of node.left + depth of node.right + 1)
	'''

	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		max_diameter = 0  # 0为最小直径(只有一个结点)

		def depth(root):
			if root is None: return 0
			ldep = depth(root.left)
			rdep = depth(root.right)
			nonlocal max_diameter
			max_diameter = max(max_diameter, ldep + rdep)
			return 1 + max(ldep, rdep)

		depth(root)
		return max_diameter


import unittest


class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution(self):
		solution = Solution()
		'''
			 1
			/ \
		   2   3
		  / \    
		 4	 5
		'''
		node1 = TreeNode(1)
		node2 = TreeNode(2)
		node3 = TreeNode(3)
		node4 = TreeNode(4)
		node5 = TreeNode(5)
		node1.left = node2
		node1.right = node3
		node2.left = node4
		node2.right = node5

		self.assertTrue(solution.diameterOfBinaryTree(node1) == 3)

		'''
			 1
			/ \
		   2   3
		  / \    
		 4	 5
		/     \
	   6       7
	  /         \
	 8           9
	   
		'''
		node1 = TreeNode(1)
		node2 = TreeNode(2)
		node3 = TreeNode(3)
		node4 = TreeNode(4)
		node5 = TreeNode(5)
		node6 = TreeNode(6)
		node7 = TreeNode(7)
		node8 = TreeNode(8)
		node9 = TreeNode(9)
		node1.left = node2
		node1.right = node3
		node2.left = node4
		node2.right = node5
		node4.left = node6
		node6.left = node8
		node5.right = node7
		node7.right = node9

		self.assertTrue(solution.diameterOfBinaryTree(node1) == 6)


if __name__ == "__main__":
	unittest.main()
