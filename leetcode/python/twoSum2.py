"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for x in range(len(nums)):
        #     for y in range(x+1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [nums[x], nums[y]]

        start,end=0,len(nums)-1
        while start<end:
            if nums[start]+nums[end]>target:
                end-=1
            elif nums[start]+nums[end]<target:
                start+=1
            elif nums[start]+nums[end]==target:
                return [nums[start],nums[end]]
            else:
                return []


print(Solution().twoSum([2,7,10,23],9))
print(Solution().twoSum([22,2,2,1,3141,7,10,23],45))