### Level1

#### [595. 大的国家](https://leetcode.cn/problems/big-countries/)

`World` 表：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | int     |
+-------------+---------+
name 是这张表的主键。
这张表的每一行提供：国家名称、所属大陆、面积、人口和 GDP 值。
```

 

如果一个国家满足下述两个条件之一，则认为该国是 **大国** ：

- 面积至少为 300 万平方公里（即，`3000000 km2`），或者
- 人口至少为 2500 万（即 `25000000`）

编写一个 SQL 查询以报告 **大国** 的国家名称、人口和面积。

按 **任意顺序** 返回结果表。

查询结果格式如下例所示。

**示例：**

```
输入：
World 表：
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
输出：
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```



SQL:

```sql
select 
name,population,area 
from world 
where area >= 3000000 or population >= 25000000;
```

#### [596. 超过5名学生的课](https://leetcode.cn/problems/classes-more-than-5-students/)

表: `Courses`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class)是该表的主键列。
该表的每一行表示学生的名字和他们注册的班级。
```

 编写一个SQL查询来报告 **至少有5个学生** 的所有班级。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。 

**示例 1:**

```
输入: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
输出: 
+---------+ 
| class   | 
+---------+ 
| Math    | 
+---------+
解释: 
-数学课有6个学生，所以我们包括它。
-英语课有1名学生，所以我们不包括它。
-生物课有1名学生，所以我们不包括它。
-计算机课有1个学生，所以我们不包括它。
```

SQL

```sql
select class from courses group by class count(distinct student) >=5;
```

#### [1757. 可回收且低脂的产品](https://leetcode.cn/problems/recyclable-and-low-fat-products/)

表：`Products`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id 是这个表的主键。
low_fats 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品是低脂产品，'N' 表示不是低脂产品。
recyclable 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品可回收，而 'N' 表示不可回收。
```

 

写出 SQL 语句，查找既是低脂又是可回收的产品编号。

返回结果 **无顺序要求** 。

查询结果格式如下例所示：

```
Products 表：
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Result 表：
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。
```

### sql

```sql
SELECT product_id from products where low_fats='Y' and recyclable ='Y'
```

#### [584. 寻找用户推荐人](https://leetcode.cn/problems/find-customer-referee/)

给定表 `customer` ，里面保存了所有客户信息和他们的推荐人。

```
+------+------+-----------+
| id   | name | referee_id|
+------+------+-----------+
|    1 | Will |      NULL |
|    2 | Jane |      NULL |
|    3 | Alex |         2 |
|    4 | Bill |      NULL |
|    5 | Zack |         1 |
|    6 | Mark |         2 |
+------+------+-----------+
```

写一个查询语句，返回一个客户列表，列表中客户的推荐人的编号都 **不是** 2。

对于上面的示例数据，结果为：

```
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

sql

```sql
select name from customer where ifnull(referee_id,0) != 2
```

#### [183. 从不订购的客户](https://leetcode.cn/problems/customers-who-never-order/)

某网站包含两个表，`Customers` 表和 `Orders` 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

`Customers` 表：

```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```

`Orders` 表：

```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```

例如给定上述表格，你的查询应返回：

```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

sql

```sql
select name as Customers from customers where not exists (select 1 from orders where orders.customerid=customers.id)
```

#### [1873. 计算特殊奖金](https://leetcode.cn/problems/calculate-special-bonus/)

#### 表: `Employees`

```
+-------------+---------+
| 列名        | 类型     |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id 是这个表的主键。
此表的每一行给出了雇员id ，名字和薪水。
```

 写出一个SQL 查询语句，计算每个雇员的奖金。如果一个雇员的id是奇数并且他的名字不是以'M'开头，那么他的奖金是他工资的100%，否则奖金为0。

Return the result table ordered by `employee_id`.

返回的结果集请按照`employee_id`排序。

查询结果格式如下面的例子所示。 

**示例 1:**

```
输入：
Employees 表:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
输出：
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
解释：
因为雇员id是偶数，所以雇员id 是2和8的两个雇员得到的奖金是0。
雇员id为3的因为他的名字以'M'开头，所以，奖金是0。
其他的雇员得到了百分之百的奖金。
```

SQL

```
select employee_id ,
case when mod(employee_id,2) =1 and name not like 'M%' then salary
else 0 end as bonus 
from Employees
order by employee_id;
```

