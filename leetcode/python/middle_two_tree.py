# middle_two_tree.py
# 中序遍历

from typing import List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归



class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res 
        self.inorder(root, res)
        return res
    
    def inorder(self, node: TreeNode, res: List) -> None:
        if not node: return 
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)
        

# 迭代
""""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stack = [], []
        curr = root
        while curr or len(stack):
            while curr:
                stack.append(curr)
                node = curr.left
            node = stack.pop()
            res.append(node.val)
            curr = node.right
        return res 
""" 



if __name__ == '__main__':
    print(Solution().inorderTraversal([1,None,2,3]))