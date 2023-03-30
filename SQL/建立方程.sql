表: Terms

+-------------+------+
| Column Name | Type |
+-------------+------+
| power       | int  |
| factor      | int  |
+-------------+------+
power 是该表的主键。
该表的每一行包含关于方程的一项的信息。
power 为范围为 [0, 100] 的整数。
factor 为范围为 [-100,100] 的整数，不能为零。
 

你有一个非常强大的程序，可以解决世界上任何一个变量的方程。传递给程序的方程必须格式化如下:

左边 (LHS) 应该包含所有的术语。
右边 (RHS) 应该是零。
LHS 的每一项应遵循 "<sign><fact>X^<pow>" 的格式，其中:
<sign> 是 "+" 或者 "-"。
<fact> 是 factor 的绝对值。
<pow> 是 power 的值。
如果幂是 1, 不要加上 "^<pow>".
例如, 如果 power = 1 并且 factor = 3, 将有 "+3X"。
如果幂是 0, 不要加上 "X" 和 "^<pow>".
例如, 如果 power = 0 并且 factor = -3, 将有 "-3"。
LHS中的幂应该按 降序排序。
编写一个 SQL 查询来构建方程。

查询结果格式如下所示。

 

示例 1:

输入: 
Terms 表:
+-------+--------+
| power | factor |
+-------+--------+
| 2     | 1      |
| 1     | -4     |
| 0     | 2      |
+-------+--------+
输出: 
+--------------+
| equation     |
+--------------+
| +1X^2-4X+2=0 |
+--------------+
Example 2:

输入: 
Terms 表:
+-------+--------+
| power | factor |
+-------+--------+
| 4     | -4     |
| 2     | 1      |
| 1     | -1     |
+-------+--------+
输出: 
+-----------------+
| equation        |
+-----------------+
| -4X^4+1X^2-1X=0 |
+-----------------+
 

select concat(group_concat(term order by power desc SEPARATOR ''), '=0') as equation
from
    (select 
    power,
    concat(
        
        
        if(factor>0,'+',''), 
        factor, 
        case power when 1 then 'X' when 0 then '' else concat('X^',power) end
    
    ) as term
    from Terms
)a 

