"""
描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

数据范围：输入的数据满足  
4≤n≤1000 
输入描述：
输入一个大于2的偶数

输出描述：
从小到大输出两个素数

示例1
输入：
20
复制
输出：
7
13
复制
示例2
输入：
4
复制
输出：
2
2
"""

n = int(input())

def isPrime(num):
    for i in range(2, int(pow(num,0.5))++1):
        if num % i == 0:
            return False
        else:
            pass
    return True 


for i in range(2, n  // 2 +1 ):
    if isPrime(i) and isPrime(n-i):
        a, b = i, n-i 
print(a);print(b)
