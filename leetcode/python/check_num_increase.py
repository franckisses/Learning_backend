"""

句子是由若干 token 组成的一个列表，token 间用 单个 空格分隔，句子没有前导或尾随空格。每个 token 要么是一个由数字 0-9 组成的不含前导零的 正整数 ，要么是一个由小写英文字母组成的 单词 。

示例，"a puppy has 2 eyes 4 legs" 是一个由 7 个 token 组成的句子："2" 和 "4" 是数字，其他像 "puppy" 这样的 tokens 属于单词。
给你一个表示句子的字符串 s ，你需要检查 s 中的 全部 数字是否从左到右严格递增（即，除了最后一个数字，s 中的 每个 数字都严格小于它 右侧 的数字）。

如果满足题目要求，返回 true ，否则，返回 false 。

链接：https://leetcode.cn/problems/check-if-numbers-are-ascending-in-a-sentence

输入：s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
输出：true
解释：句子中的数字是：1, 3, 4, 6, 12 。
这些数字是按从左到右严格递增的 1 < 3 < 4 < 6 < 12 。

"""

class Solution:
    def areNumberascending(self, s: str) -> bool:
        num_list = [x for x in s.split() if x.isdigit()]
        for i in range(1, len(num_list)-1):
            if num_list[i-1] > num_list[i]:
                return False
        return True



if __name__ == '__main__':
    a = Solution()
    b = a.areNumberascending('1 this is agood 2 max 3')
    print(b)
