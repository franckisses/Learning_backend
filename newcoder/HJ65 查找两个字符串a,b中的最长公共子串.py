"""
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

数据范围：字符串长度1≤length≤300 
进阶：时间复杂度：O(n 3) ，空间复杂度：
 
O(n) 
输入描述：
输入两个字符串

输出描述：
返回重复出现的字符
示例1
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw

输出：
jklmnop

"""

a = input()
b = input()

def solution(a,b):
    if len(b) < len(a):
        a,b = b,a
    mxlen = 0 
    res = ''
    for i in range(len(a)):
        for j in range(1+i+mxlen,len(a)+1):
            sub = a[i:j]
            if sub in b:
                res = sub
                mxlen = j -i 
    print(res)

solution(a,b)
