"""
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）


数据范围：  1≤n≤2×10^ 9+14 
输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。

示例1
180

2 2 3 3 5

"""

import math 

num = int(input())
s = ''
prime = 2
while prime < math.sqrt(num)+1:
    if num % prime != 0:
        prime += 1
    else:
        num = num // prime
        s += str(prime) + ' '
        prime = 2
if num >=2:
    s += str(num) + ' '

print(s) 