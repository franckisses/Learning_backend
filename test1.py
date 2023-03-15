"""
两个数组的交集# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1：# 输入：nums1 = [1,2,2,1], nums2 = [2,2]# 输出：[2,2]
# 示例 2:# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]# 输出：[4,9]
"""
def subunion(nums1, nums2):
    
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2, nums1

    result = []
    for i in nums1:
        if i in nums2:
            result.append(i)
            nums2.remove(i)

    print(result)

subunion([1,2,2,1],[2,2])
subunion([4,9,5],[9,4,9,8,4])