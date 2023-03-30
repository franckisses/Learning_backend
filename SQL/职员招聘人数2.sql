表: Candidates

+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| experience  | enum |
| salary      | int  |
+-------------+------+
employee_id是此表的主键列。
经验是一个枚举，其中包含一个值（“高级”、“初级”）。
此表的每一行都显示候选人的id、月薪和经验。
每个候选人的工资保证是 唯一 的。
 

一家公司想雇佣新员工。公司的工资预算是 7 万美元。公司的招聘标准是：

继续雇佣薪水最低的高级职员，直到你不能再雇佣更多的高级职员。
用剩下的预算雇佣薪水最低的初级职员。
继续以最低的工资雇佣初级职员，直到你不能再雇佣更多的初级职员。
编写一个SQL查询，查找根据上述条件雇用职员的 ID。
按 任意顺序 返回结果表。
查询结果格式如下例所示。

 

示例 1:

输入:
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 15000  |
| 2           | Senior     | 20000  |
| 11          | Senior     | 16000  |
| 13          | Senior     | 50000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
输出: 
+-------------+
| employee_id |
+-------------+
| 11          |
| 2           |
| 1           |
| 9           |
+-------------+
解释: 
我们可以雇佣2名具有ID（11,2）的高级员工。由于预算是7万美元，他们的工资总额是3.6万美元，我们还有3.4万美元，但他们不足以雇佣ID为 13 的高级职员。
我们可以雇佣2名ID为（1,9）的初级员工。由于剩余预算为3.4万美元，他们的工资总额为2.5万美元，我们还有9000美元，但他们不足以雇佣ID为 4 的初级员工。
示例 2:

输入:
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 25000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 85000  |
| 11          | Senior     | 80000  |
| 13          | Senior     | 90000  |
| 4           | Junior     | 30000  |
+-------------+------------+--------+
输出: 
+-------------+
| employee_id |
+-------------+
| 9           |
| 1           |
| 4           |
+-------------+
解释: 
我们不能用目前的预算雇佣任何高级员工，因为我们需要至少 80000 美元来雇佣一名高级员工。
我们可以用剩下的预算雇佣三名初级员工。


with test as (
select employee_id , experience
, sum(salary) over(partition by experience order by salary) as total_salary 
from Candidates
)
select employee_id from test where experience='Senior' and total_salary <= 70000
union all 
select employee_id from test where experience='Junior' and total_salary <= 70000 -(select if(total_salary,max(total_salary),0) from test where experience='Senior' and total_salary <= 70000  order by total_salary desc limit 1)
