#  -*- coding: utf-8 -*-
# Author: Conan0xff
# Mail  : 1526840124@qq.com
# Func  : leetcode_301

'''
Description:

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        Args: str
        Returns: list of str
        """

        def isvalid(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                    # 某个右括号左边没有对应的左括号直接返回false
                    if count < 0:
                        return False
            return count == 0

        # 广度优先搜索
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            # 更新下一层
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}


import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        solution = Solution()
        s = "()())()"
        self.assertSetEqual(set(solution.removeInvalidParentheses(s)), set(["()()()", "(())()"]))
        s = "(a)())()"
        self.assertSetEqual(set(solution.removeInvalidParentheses(s)), set(["(a)()()", "(a())()"]))
        s = ")("
        self.assertSetEqual(set(solution.removeInvalidParentheses(s)), set([""]))


if __name__ == "__main__":
    unittest.main()
