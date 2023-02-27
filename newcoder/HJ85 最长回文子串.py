"""
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
数据范围：字符串长度1≤s≤350 
进阶：时间复杂度：
O(n) ，空间复杂度：O(n) 
输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度

示例1
输入：
cdabbacc
复制
输出：
4
复制
说明：
abba为最长的回文子串   
"""


my_str = input()

def func(str_input):
    max_len = 0
    for i in range(len(str_input)):
        for j in range(len(str_input) -1, i-1, -1):
            if str_input[i: j + 1][::-1] == str_input[i: j + 1]:
                if j + 1 -i > max_len:
                    max_len = j + 1 -i 
    return max_len

print(func(my_str))

