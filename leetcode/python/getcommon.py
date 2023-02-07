# -*- coding: utf-8 -*-

# @Time: 2023-02-05
# @File: %
# @Author: dreamhomes
# @Description: 
"""

给你两个整数数组 nums1 和 nums2 ，它们已经按非降序排序，请你返回两个数组的 最小公共整数 。如果两个数组 nums1 和 nums2 没有公共整数，请你返回 -1 。

如果一个整数在两个数组中都 至少出现一次 ，那么这个整数是数组 nums1 和 nums2 公共 的。

 

示例 1：

输入：nums1 = [1,2,3], nums2 = [2,4]
输出：2
解释：两个数组的最小公共元素是 2 ，所以我们返回 2 。
示例 2：

输入：nums1 = [1,2,3,6], nums2 = [2,3,4,5]
输出：2
解释：两个数组中的公共元素是 2 和 3 ，2 是较小值，所以返回 2 。
 

提示：

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
nums1 和 nums2 都是 非降序 的。

answer:
    class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        j, m = 0, len(nums2)
        for x in nums1:
            while j < m and nums2[j] < x:  # 找下一个 nums2[j] >= x
                j += 1
            if j < m and nums2[j] == x:
                return x
        return -1


"""


class Solution:
    def getCommon(self, nums1, nums2):
        # return min(set(nums1) & set(nums2), default=-1)

        # 双指针 归并排序
        i, x = 0, len(nums1)
        m, y = 0, len(nums2)
        while i < x and m < y:
            if nums1[i] == nums2[m]:
                return nums1[1]
            elif nums1[i] > nums2[m]:
                m += 1
            else:
                i += 1
        return -1
if __name__ == '__main__':
    a = Solution()
    print(a.getCommon([1, 2, 3, 4], [2, 3, 6, 8]))

