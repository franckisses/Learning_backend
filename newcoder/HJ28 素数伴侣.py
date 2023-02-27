"""题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。
输出:

输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
数据范围： 
1≤n≤100  ，输入的数据大小满足 2≤val≤30000 
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。
输入：
4
2 5 6 13
输出：
2
示例2
输入：
2
3 6
输出：
0

"""
def is_prime(num):
    if num<2:
        return False
    i = 2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True
     
def find(odd, evens, visited, selected):
    for i, even in enumerate(evens):
        if is_prime(even+odd) and not visited[i]:
            visited[i]=True  
            # 如果当前偶数没有对象（0），那么就与之组合
            # 就尝试为 selected[i] 协调新对象
            if selected[i] == 0 or find(selected[i],  evens, visited, selected):
                selected[i]=odd
                return True
    # 没有对象
    return False
 
while True:
    try:
        n=int(input())
        nums=list(map(int,input().split(' ')))
        
        # 准备分组
        evens, odds=[], []
        for num in nums:
            if num%2==0:
                evens.append(num)
            else:
                odds.append(num)

        # 尝试为每个奇数匹配偶数        
        selected=[0]*len(evens)    # 记录与第 i 个偶数匹配的奇数
        result = 0
        for odd in odds:
            visited=[0]*len(evens) # 记录访问过的偶数，防止重复访问
            if find(odd, evens, visited, selected):
                result +=1 #匹配成功就把结果+1
        print(result)
    except:
        break