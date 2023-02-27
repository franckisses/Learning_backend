"""
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：

1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

输入描述：
输入正整数N（N不大于100）

输出描述：
输出一个N行的蛇形矩阵。

示例1
输入：
4

输出：
1 3 6 10
2 5 9
4 8
7"""

while 1:
    try:
        # create nested list [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
        n = int(input())
        list1 = []
        for i in range(1,n+1):
            list1.append([0]*i)
        a = 0

        # insert num to the list 
        for i in range(n):
            for j in range(i+1):
                a = a + 1
                list1[i][j]=a

        # loop get last list append to the new result
        list2,she = [],[]
        for i in range(1,n+1):
            for line in list1:
                if line:
                    list2.append(line.pop(-1))
            she.append(" ".join(map(str,list2)))
            list2 = []
        for i in she:
            print(i)
    except:
        break
