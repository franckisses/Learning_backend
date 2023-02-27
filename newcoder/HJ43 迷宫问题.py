"""
描述
定义一个二维数组 N*M ，如 5 × 5 数组下所示：


int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};


它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。


数据范围： 2≤n,m≤10  ， 输入的内容只包含 0≤val≤1 

输入描述：
输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出描述：
左上角到右下角的最短路径，格式如样例所示。

示例1
输入：
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

输出：
(0,0)
(1,0)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
(3,4)
(4,4)

示例2
输入：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 1
0 1 1 1 0
0 0 0 0 0

输出：
(0,0)
(1,0)
(2,0)
(3,0)
(4,0)
(4,1)
(4,2)
(4,3)
(4,4)


说明：
注意：不能斜着走！！   """

def dfs(i, j):
    walk =[(0,1), (0,-1), (1,0), (-1,0)]
    if i == m-1 and i == n-1:
        for p in path:
            print("({x},{y})".format(x=p[0],y=p[1]))
        return 
    for w in walk:
        x = i + w[0]
        y = j + w[1]

while 1:
    try:
        lst = []
        m, n = list(map(int, input().split()))
        for _ in range(m):
            lst.append(list(map(int, input().split())))

        path = [(0,0)]
        lst[0][0] = 1
        dfs(0,0) 
    except:
        break  