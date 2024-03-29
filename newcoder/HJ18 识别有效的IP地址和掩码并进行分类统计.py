"""
描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址从1.0.0.0到126.255.255.255;

B类地址从128.0.0.0到191.255.255.255;

C类地址从192.0.0.0到223.255.255.255;

D类地址从224.0.0.0到239.255.255.255；

E类地址从240.0.0.0到255.255.255.255


私网IP范围是：

从10.0.0.0到10.255.255.255

从172.16.0.0到172.31.255.255

从192.168.0.0到192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
（注意二进制下全是1或者全是0均为非法子网掩码）

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。

请参考帖子https://www.nowcoder.com/discuss/276处理循环输入的问题。
输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1

10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0

1 0 1 0 0 2 1
说明：
10.70.44.68~255.254.255.0的子网掩码非法，19..0.~255.255.255.0的IP地址非法，所以错误IP地址或错误掩码的计数为2；
1.0.0.1~255.0.0.0是无误的A类地址；
192.168.0.2~255.255.255.0是无误的C类地址且是私有IP；
所以最终的结果为1 0 1 0 0 2 1 

0.201.56.50~255.255.111.255
127.201.56.50~255.255.111.255

输出：
0 0 0 0 0 0 0
说明：
类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
"""

import re

A, B, C, D, E, errs, privates = 0, 0, 0, 0, 0, 0, 0


def getBin(string):
    string_bin = ''
    for i in string.split('.'):
        string_bin += bin(int(i))[2:].rjust(8, '0')
    return string_bin


try:
    while True:
        ip, mask = input().split('~')
        mask_bin = getBin(mask)
        if ip.split('.')[0] in ('0', '127'):
            continue
        elif mask in ('0.0.0.0', '255.255.255.255'):
            errs += 1
            continue
        else:
            if re.search('01', mask_bin):
                errs += 1
                continue
        ip_bin = getBin(ip)
        if re.search(r'\.\.', ip):
            errs += 1
        elif getBin('1.0.0.0') < ip_bin < getBin('126.255.255.255'):
            A += 1
            if getBin('10.0.0.0') < ip_bin < getBin('10.255.255.255'):
                privates += 1
        elif getBin('128.0.0.0') < ip_bin < getBin('191.255.255.255'):
            B += 1
            if getBin('172.16.0.0') < ip_bin < getBin('172.31.255.255'):
                privates += 1
        elif getBin('192.0.0.0') < ip_bin < getBin('223.255.255.255'):
            C += 1
            if getBin('192.168.0.0') < ip_bin < getBin('192.168.255.255'):
                privates += 1
        elif getBin('224.0.0.0') < ip_bin < getBin('239.255.255.255'):
            D += 1
        elif getBin('240.0.0.0') < ip_bin < getBin('255.255.255.255'):
            E += 1
except (EOFError, ValueError):
    pass
print(A, B, C, D, E, errs, privates)
