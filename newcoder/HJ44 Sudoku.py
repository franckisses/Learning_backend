"""问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个3X3粗线宫内的数字均含1-9，并且不重复。
例如：
数据范围：输入一个 9*9 的矩阵
输入描述：
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述：
完整的9X9盘面数组

示例1
输入：
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
复制
输出：
5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1"""




class Solution:

    def isValue(self, board, x, y):
        # 检查已经填入的坐标是否和列中有的元素相等
        for i in range(9): 
            if i != x and board[i][y] == board[x][y]:
                return False
        # 检查已经填入的坐标是否和行中有的元素相等
        for j in range(9): 
            if j != y and board[x][j] == board[x][y]:
                return False

        # 检查每个正方形是否符合（粗线框内只有1~9） 
        m, n = 3*(x // 3), 3*(y // 3)  # 这里求出的是3x3网格的左上角的坐标 
        for i in range(3):
            for j in range(3):
                if(i+m != x or j+n != y) and board[i+m][j+n] == board[x][y]:
                    return False  

        return True

    def dfs(self, board):

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for k in '123456789':  # 从里面选择一个
                        board[i][j] = int(k)
                        if self.isValue(board, i, j) and self.dfs(board):
                            return True
                        # 回溯
                        board[i][j] = 0
                    # 都不行，说明上次的数字不合理
                    return False
        # 全部便利完，返回True
        return True

while True:
    try:
        board = []
        for i in range(9):
            row = list(map(int, input().split()))
            board.append(row)

        s = Solution()
        s.dfs(board)

        for i in range(9):
            board[i] = list(map(str, board[i]))
            print(' '.join(board[i]))
    except:
        break

