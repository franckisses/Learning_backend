# -*- coding: utf-8 -*-

# @Time: 2023-02-11
# @File: %
# @Author: dreamhomes
# @Description: 


"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c == ')' and stack and stack[-1] =='(':
                stack.pop()
            elif c == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif c =='}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return not stack


if __name__ == '__main__':
    a = Solution()
    print(a.isValid('[()]'))

