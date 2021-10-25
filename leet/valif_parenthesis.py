"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_par = []

        for char in s:
            if self._is_open(char):
                open_par.append(char)
            elif len(open_par) > 0 and self._is_pair(open_par[-1], char):
                open_par.pop()
            else:
                return False

        return open_par == []

    def _is_open(self, char: str) -> bool:
        if char in {'(', '[', '{'}:
            return True
        else:
            return False

    def _is_pair(self, par1: str, par2: str) -> bool:
        parenthesis = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        if parenthesis[par1] == par2:
            return True
        else:
            return False
