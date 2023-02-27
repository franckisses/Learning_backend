# binaryTreePaths.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Definition for a binary tree node.
        if not root:
            return []
        # 初始化递归栈、路径栈和结果集
        stack = [root]
        stackPath = []
        res = []
        stackPath.append(str(root.val))

        while stack:
            # 节点和路径出栈
            node = stack.pop()
            path = stackPath.pop()
            # 如果当前节点为叶子节点
            if node.left == None and node.right == None:
                res.append(path)
            # 右子树入栈
            if node.right:
                stack.append(node.right)
                stackPath.append(path + "->" + str(node.right.val))
            # 左子树入栈
            if node.left:
                stack.append(node.left)
                stackPath.append(path + "->" + str(node.left.val))

        return res
