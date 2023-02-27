# -*- coding: utf-8 -*-

# @Time: 2023-02-11
# @File: %
# @Author: dreamhomes
# @Description: 

"""
给你一个非负整数 x ，算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

 

示例 1：

输入：x = 4
输出：2
示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
 

提示：

0 <= x <= 231 - 1

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1 
        low, high = 0, x // 2
        while low < high-1:
            mid =  low + (high - low) // 2
            if mid ** 2 < x:
                low = mid
            elif mid ** 2 > x:
                high = mid
            else:
                return mid

        if low**2 == x:
            return low
        elif high**2 == x:
            return high
        return high if high**2 < x else low


if __name__ == '__main__':
    a = Solution()
    print(a.mySqrt(6))
