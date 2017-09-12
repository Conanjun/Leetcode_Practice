#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_20

'''
Description:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

from DataStructure.Stack import Stack


class Solution(object):
    def isValid(self,s):
        """
        Args: str
        Returns: bool
        """
        stack = Stack()
        # 以后面的parenthese为key可方便出栈取值比较
        parentheses = {']': '[', ')': '(', '}': '{'}
        for i in s:
            if i in parentheses.values():
                stack.push(i)
            elif i in parentheses.keys():
                if stack.isEmpty() or parentheses[i] != stack.pop():
                    return False
        return stack.isEmpty()


import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        solution = Solution()
        s = "()"
        self.assertTrue(solution.isValid(s))
        s = "()[]{}"
        self.assertTrue(solution.isValid(s))
        s = "(]"
        self.assertFalse(solution.isValid(s))
        s = "([)]"
        self.assertFalse(solution.isValid(s))


if __name__ == "__main__":
    unittest.main()
