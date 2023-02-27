"""
描述
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。

注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
数据范围：字符串长度：1≤s≤150 
进阶：时间复杂度：O(n 3 ) ，空间复杂度：O(n) 
输入描述：
输入两个只包含小写字母的字符串

输出描述：
输出一个整数，代表最大公共子串的长度

示例1
输入：
asdfas
werasdfaswer
输出：
6"""

while True:
    try:
        a, b = input(), input()
        if len(a) > len(b):
            a, b = b, a # a存短，b存长
        Max = 0
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i:j+1] in b and j + 1 - i > Max:
                    Max = j + 1 - i
        print(Max)
    except:
        break
