
"""
翻转二叉树

https://leetcode.cn/problems/invert-binary-tree/?company_slug=sensetime

"""
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def interTree(self, root: TreeNode) -> List:
        if not root: return 
        root.left , root.right = root.right, root.left

        self.interTree(root.left)
        self.interTree(root.right)

        return root 
    