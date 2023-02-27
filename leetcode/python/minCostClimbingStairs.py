"""



"""
from typing import List




class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)       #初始化数组,dp[i]代表的是爬到第i个台阶所需的最小费用，最后一台阶其实理论是顶部(不是真的台阶)
        dp[0],dp[1]=0,0            #设置起始值
        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])    #有两种走法，取费用小的
            print(dp)
        return dp[-1]


print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

