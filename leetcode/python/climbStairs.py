# -*- coding: utf-8 -*-

# @Time: 2023-02-11
# @File: %
# @Author: dreamhomes
# @Description: 

"""

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        s = [1, 2]
        if n <=2:
            return s[n-1]
        else:
            while len(s) < n:
                s.append(s[-1]+ s[-2])
        return s[-1]

if __name__ =='__main__':
    a = Solution()
    print(a.climbStairs(4))        
