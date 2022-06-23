## 窗口函数

## 窗口的由来：

	1. 窗口函数也称为OLAP 函数。
	1. 通过partition by 分组之后的记录集合称为窗口

## 应用场景

1. 用于分区排序。
2. 动态group by
3. Top N
4. 累计计算
5. 层次查询

## 窗口函数的种类

1. 聚合函数（SUM, AVG, COUNT, MAX, MIN)
2. RANK, DENSE_RANK, ROW_NUMBER 等专用窗口函数

RANK 函数，统计时，如果有3个并列第一，则排序的记录为 1,1,1,4

DENSE_RANK函数，统计时，如果有3个并列第一，则顺序记录为: 1,1,1,2

ROW_NUMBER 函数，统计时。赋予唯一的连续位次，如果三个并列第一。则顺序为：1,2,3,4

Rank:

```sql
-- 根据JOB 进行分组，通过sla从大到小排序。
select ename,job,sla
, rank over (parition by job order by sla desc) as rankin
, dense_rank over (parition by job order by sla desc) as rankin 
, row_number over (parition by job order by sla desc) as rankin
frin emp;
```

**ATTENTIONS:**

   窗口函数不能载WHERE 字句，或者 GROUP BY 子句中使用。

​	因为窗口函数其实已经在分组聚合之后，进行排序了。

   如果在窗口函数的语句中使用WHERE 字句，相当于已经分好组之后再对结果进行过滤，那么之前的分组就是不准确。

#### 作为窗口函数使用聚合函数

```sql
select name, price
, sum(price) over (order by name) as current_sum
from product;
-- CURRNET_SUM 	相当于前面的累计；
```

#### 指定框架

```sql
select name, price
avg(price) over (order by name rows 2 preceding) as moving_avg
from product;
---------------------
name    price.     moving_avg
1.      50. 			50.000
2. 			15				32.500
3.			50				36.333
4.  		10 				25.000 
取前面两个，一共三个cell 的数进行求平均
```

#### 计算移动平均 -指定前边一行和后边一行

```sql
select name,price,
avg(price) over(order by name rows between 1 preceding and 1 following) as moving_avg
from product;
---------------------
name    price.     moving_avg
1.      50. 			32.500
2. 			15				38.333
3.			50				25.000
4.  		10 				30.000

```

