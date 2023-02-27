"""描述
IPV4地址可以用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此正号不需要出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。

现在需要你用程序来判断IP是否合法。

数据范围：数据组数：1≤t≤18 
进阶：时间复杂度：O(n) ，空间复杂度：O(n) 

输入描述：
输入一个ip地址，保证不包含空格

输出描述：
返回判断的结果YES or NO

示例1
输入：
255.255.255.1000

输出：
NO
"""
while True:
    try:
        s = input().split('.')
        c = 0  # 计数器，指导‘YES’输出
        if len(s) != 4:  # 位数不够4，直接NO
            print('NO')
            continue
        for i in s:
            if not i.isdigit():  # 存在非数字字符，直接NO
                print('NO')
                continue
            elif int(i) > 255 or (i.startswith('0') and len(i) > 1):  # 最大值大于255 或者数字为'03'这种格式的，NO
                print('NO')
                continue
            else:
                c +=1
        if c ==4:  # 计数器，4次循环结束后再执行YES输出
            print('YES')
    except:
        break
