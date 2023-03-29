
表: Calls

+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
+--------------+----------+
(caller_id, recipient_id, call_time) 是这个表的主键。
每一行所含的时间信息都是关于caller_id 和recipient_id的。
 

编写一个 SQL 查询来找出那些ID们在任意一天的第一个电话和最后一个电话都是和同一个人的。这些电话不论是拨打者还是接收者都会被记录。

结果请放在一个任意次序约束的表中。

查询结果格式如下所示：

输入：
Calls table:
+-----------+--------------+---------------------+
| caller_id | recipient_id | call_time           |
+-----------+--------------+---------------------+
| 8         | 4            | 2021-08-24 17:46:07 |
| 4         | 8            | 2021-08-24 19:57:13 |
| 5         | 1            | 2021-08-11 05:28:44 |
| 8         | 3            | 2021-08-17 04:04:15 |
| 11        | 3            | 2021-08-17 13:07:00 |
| 8         | 11           | 2021-08-17 22:22:22 |
+-----------+--------------+---------------------+
输出：
+---------+
| user_id |
+---------+
| 1       |
| 4       |
| 5       |
| 8       |
+---------+
解释：
在 2021-08-24，这天的第一个电话和最后一个电话都是在user 8和user 4之间。user8应该被包含在答案中。
同样的，user 4在2 021-08-24 的第一个电话和最后一个电话都是和user 8的。user 4也应该被包含在答案中。
在 2021-08-11，user 1和5有一个电话。这个电话是他们彼此当天的唯一一个电话。因此这个电话是他们当天的第一个电话也是最后一个电话，他们都应该被包含在答案中。



with base as (
    select caller_id as talker, recipient_id as another_talker,call_time from Calls 
    union all 
    select recipient_id, caller_id, call_time from Calls 
), temp as (
    select 
    talker,another_talker
    , date(call_time) as date 
     , rank() over(partition by date_format(call_time,'%Y-%m-%d'),talker order by call_time ) as rk1
    , rank() over(partition by date_format(call_time,'%Y-%m-%d'),talker order by call_time desc) as rk2
    from base 
)
select distinct t.talker as user_id from temp t 
left join (select date, talker, another_talker from temp where rk2 = 1) tt
on t.date = tt.date and t.talker = tt.talker
where rk1 = 1 and t.another_talker = tt.another_talker
order by t.talker
