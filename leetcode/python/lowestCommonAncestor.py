
"""
由于lowestCommonAncestor(root, p, q)的功能是找出以root为根节点的两个节点p和q的最近公共祖先。 我们考虑：

如果p和q分别是root的左右节点，那么root就是我们要找的最近公共祖先
如果root是None，说明我们在这条寻址线路没有找到，我们返回None表示没找到
我们继续在左右子树执行相同的逻辑。
如果左子树没找到，说明在右子树，我们返回lowestCommonAncestor(root.right, p , q)
如果右子树没找到，说明在左子树，我们返回lowestCommonAncestor(root.left, p , q)
如果左子树和右子树分别找到一个，我们返回root
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left,  p , q)
        r = self.lowestCommonAncestor(root.right,  p , q)
        return root if l and r else l or r