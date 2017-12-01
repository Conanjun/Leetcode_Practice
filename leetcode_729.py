#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_729


'''
	 My Calendar I 
	
   Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:
The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

'''


# ***********************************************************************************************************************
class Node(object):
	def __init__(self, s, e):
		self.s = s
		self.e = e
		self.left = None
		self.right = None


# ***********************************************************************************************************************
class MyCalendar(object):
	def __init__(self):
		self.root = None

	# 将每个实例看成一个结点，有三种情况：
	# 1.新插入结点的start大于P结点的end，则将新插入结点插入到P结点的右子树，P = P.left。
	# 2.新插入结点的end小于P结点的start，则将新插入结点插入到P结点的左子树，P = P.right。
	# 3.新插入结点的范围跟P结点的范围有重叠，则返回false。
	def book(self, start, end):
		"""
		:type start: int
		:type end: int
		:rtype: bool
		"""
		if not self.root:
			self.root = Node(start, end)
			return True
		else:
			return self.book_helper(start,end,self.root)

	# 无法插入新实例的时候返回false
	def book_helper(self, start, end, node):
		if start >= node.e:
			if node.right:
				return self.book_helper(start, end, node.right)
			else:
				node.right = Node(start, end)
				return True
		elif end <= node.s:
			if node.left:
				return self.book_helper(start, end, node.left)
			else:
				node.left = Node(start, end)
				return True
		else:
			return False


import unittest


class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution(self):
		mc=MyCalendar()
		self.assertTrue(mc.book(10,20))
		self.assertFalse(mc.book(15,25))
		self.assertTrue(mc.book(20,30))

if __name__ == "__main__":
	unittest.main()
