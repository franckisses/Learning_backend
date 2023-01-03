"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

 

示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3

"""
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def find_lower(num, length):
            # 关键函数，计算index处的值为num时，其往左或者往右需要延伸length长度时需要的最小数值和
            if num > length:
                # 序列为num-1,num-2...,num-length
                return length * (2 * num - 1 - length) // 2
            # 序列为num-1,num-2,...,1以及length-num+1个1
            return (num - 1) * num // 2 + length - num + 1

        def check(num):
            # 计算index为num时所需的最小数值和
            res = num
            # 左边
            res += find_lower(num, index)
            # 右边
            res += find_lower(num, n - index - 1)
            return res <= maxSum

        # 边界条件
        low = 1
        high = maxSum
        while low < high - 1:
            mid = low + (high - low) // 2
            if check(mid):
                low = mid
            else:
                high = mid
        return high if check(high) else low

