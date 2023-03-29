表: Candidates

+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| experience  | enum |
| salary      | int  |
+-------------+------+
employee_id是此表的主键列。
经验是包含一个值（“高级”、“初级”）的枚举类型。
此表的每一行都显示候选人的id、月薪和经验。
 

一家公司想雇佣新员工。公司的工资预算是 70000 美元。公司的招聘标准是：

雇佣最多的高级员工。
在雇佣最多的高级员工后，使用剩余预算雇佣最多的初级员工。
编写一个SQL查询，查找根据上述标准雇佣的高级员工和初级员工的数量。
按 任意顺序 返回结果表。
查询结果格式如下例所示。

 

示例 1:

输入: 
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 20000  |
| 11          | Senior     | 20000  |
| 13          | Senior     | 50000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
输出: 
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 2                   |
| Junior     | 2                   |
+------------+---------------------+
说明：
我们可以雇佣2名ID为（2,11）的高级员工。由于预算是7万美元，他们的工资总额是4万美元，我们还有3万美元，但他们不足以雇佣ID为13的高级员工。
我们可以雇佣2名ID为（1,9）的初级员工。由于剩下的预算是3万美元，他们的工资总额是2万美元，我们还有1万美元，但他们不足以雇佣ID为4的初级员工。
示例 2：
输入: 
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 80000  |
| 11          | Senior     | 80000  |
| 13          | Senior     | 80000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
输出: 
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 0                   |
| Junior     | 3                   |
+------------+---------------------+
解释：
我们不能用目前的预算雇佣任何高级员工，因为我们需要至少80000美元来雇佣一名高级员工。
我们可以用剩下的预算雇佣三名初级员工。



with temp as (
    select employee_id, experience,
    sum(salary) over (partition by experience order by salary) cost
    from Candidates
)
select 'Senior' experience, count(cost) as accepted_candidates from temp
where experience='Senior' and cost<=70000
union all
select 'Junior' experience, count(cost) as accepted_candidates from temp
where experience='Junior'
and
cost<=70000-(select if(max(cost)<=70000, max(cost), 0) as ct from temp where experience='Senior' and cost<=70000);
