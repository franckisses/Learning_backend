# sortedArrayToBST.py
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Definition for a binary tree node.
        def make_tree(start_index, end_index): #只和长度有关
            #首先判定我们的区间是否合理，即left_index要<=right_index
            #当相等时，只有root会产生，不会产生左右小树
            if start_index > end_index:
                return None
            
            #我这里变量名都写得比较长，目的是方便理解
            mid_index = (start_index + end_index)//2
            this_tree_root = TreeNode(nums[mid_index]) #做一个小树的root

            this_tree_root.left = make_tree(start_index,mid_index-1)
            this_tree_root.right = make_tree(mid_index+1, end_index)

            return this_tree_root #做好的小树
        
        return make_tree(0,len(nums)-1) 
        #可以看到整个题解只和index有关，和数组里的具体数字无关，
        #因为题目给出的“有序数列”帮助我们满足了“二叉搜索树”的条件。