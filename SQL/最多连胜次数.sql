2173. 最多连胜的次数
难度
困难

5

收藏

分享
切换为英文
接收动态
反馈
SQL架构
表: Matches

+-------------+------+
| Column Name | Type |
+-------------+------+
| player_id   | int  |
| match_day   | date |
| result      | enum |
+-------------+------+
(player_id, match_day) 是该表的主键。
每一行包括了：参赛选手 id、 比赛时间、 比赛结果。
比赛结果（result）的枚举类型为 ('Win', 'Draw', 'Lose')。
 

选手的 连胜数 是指连续获胜的次数，且没有被平局或输球中断。

写一个SQL 语句来计算每个参赛选手最多的连胜数。

结果可以以任何顺序返回。

结果格式如下例所示：

 

示例 1:

输入: 
Matches 表:
+-----------+------------+--------+
| player_id | match_day  | result |
+-----------+------------+--------+
| 1         | 2022-01-17 | Win    |
| 1         | 2022-01-18 | Win    |
| 1         | 2022-01-25 | Win    |
| 1         | 2022-01-31 | Draw   |
| 1         | 2022-02-08 | Win    |
| 2         | 2022-02-06 | Lose   |
| 2         | 2022-02-08 | Lose   |
| 3         | 2022-03-30 | Win    |
+-----------+------------+--------+
输出: 
+-----------+----------------+
| player_id | longest_streak |
+-----------+----------------+
| 1         | 3              |
| 2         | 0              |
| 3         | 1              |
+-----------+----------------+
解释: 
Player 1:
从 2022-01-17 到 2022-01-25, player 1连续赢了三场比赛。
2022-01-31, player 1 平局.
2022-02-08, player 1 赢了一场比赛。
最多连胜了三场比赛。

Player 2:
从 2022-02-06 到 2022-02-08, player 2 输了两场比赛。
最多连赢了0场比赛。

Player 3:
2022-03-30, player 3 赢了一场比赛。
最多连赢了一场比赛。

 两遍排序，按照日期和结果进行排序，会有ID差。然后进行聚合，取最高的。

"""

with m as(
    select player_id,match_day,result,
    row_number() over (partition by player_id order by match_day) rk1,
    row_number() over (partition by player_id,result order by match_day) rk2
    from Matches
),
n as(
    select player_id,sum(result='Win') num from m group by player_id,rk1 - rk2
)
select player_id,max(num) longest_streak from n group by player_id


"""
