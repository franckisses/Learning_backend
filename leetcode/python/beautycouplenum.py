# -*- coding: utf-8 -*-

# @Time: 2023-01-04
# @File: %
# @Author: dreamhomes
# @Description: 

"""
https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/
给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。

漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[j]) <= high 。

 

示例 1：

输入：nums = [1,4,2,7], low = 2, high = 6
输出：6
解释：所有漂亮数对 (i, j) 列出如下：
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
示例 2：

输入：nums = [9,8,4,2,1], low = 5, high = 14
输出：8
解释：所有漂亮数对 (i, j) 列出如下：
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 2 * 104
1 <= low <= high <= 2 * 104

"""

class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.child = {}
        self.cnt = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,num):
        node = self.root
        for j in range(15,-1,-1):
            val = num >> j & 1
            if val not in node.child:
                node.child[val] = TrieNode(val)
            node.cnt += 1
            node = node.child[val]
        node.cnt += 1
    
    def query(self,num,target):
        # 返回 与num异或 <= target的 有多少对
        node = self.root
        res = 0
        for j in range(15, -1, -1):
            # 我们想维护一个异或值，这个值始终和target保持相同前缀
            val = num >> j & 1
            cur = target >> j & 1
            if cur:
                # target 当前位是1，我们要维护的异或结果由于在此之前跟target每一位的数字都相同，唯独当前位，如果取了0，不管以后的位怎么取都严格小于target，满足条件
                # 于是，问题就是当前位在target为1的条件下，何时能取得0？当然是当前位有 val 这个child时可以
                if val in node.child:
                    res += node.child[val].cnt
                if 1-val not in node.child:
                    # 如果当前位没法和target当前位相同，都取到1，则可以直接return了
                    return res
                node = node.child[1-val]
            else:
                # target 当前位是0，我们要维护的异或结果当前位必须也取0, 并且取1不会贡献任何res，因为比target大了
                # 如何取0呢？
                if val not in node.child:
                    # 如果当前位没法和target当前位相同，都取到0，则可以直接return了
                    return res
                node = node.child[val]
        res += node.cnt
        # 这里是假设能跟target一模一样，则继续加上cnt，这也是为什么返回的是小于等于
        return res
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        ans = 0
        for num in nums:
            trie.add(num)
            ans +=  trie.query(num, high) - trie.query(num, low-1)
        return ans
