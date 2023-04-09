
表: Keywords

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| topic_id    | int     |
| word        | varchar |
+-------------+---------+
(topic_id, word) 是该表的主键。
该表的每一行都包含一个主题的 id 和一个用于表达该主题的词。
可以用多个词来表达同一个主题，也可以用一个词来表达多个主题。
 

表: Posts

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| post_id     | int     |
| content     | varchar |
+-------------+---------+
post_id 是该表的主键。
该表的每一行都包含一个帖子的 ID 及其内容。
内容仅由英文字母和空格组成。
 

Leetcode 从其社交媒体网站上收集了一些帖子，并对每个帖子的主题感兴趣。每个主题可以由一个或多个关键字表示。如果某个主题的关键字存在于一个帖子的内容中 (不区分大小写)，那么这个帖子就有这个主题。

编写一个 SQL 查询，根据以下规则查找每篇文章的主题:

如果帖子没有来自任何主题的关键词，那么它的主题应该是 "Ambiguous!"。
如果该帖子至少有一个主题的关键字，其主题应该是其主题的 id 按升序排列并以逗号 '，' 分隔的字符串。字符串不应该包含重复的 id。
以 任意顺序 返回结果表。

查询结果格式如下所示。

示例 1:

输入: 
Keywords 表:
+----------+----------+
| topic_id | word     |
+----------+----------+
| 1        | handball |
| 1        | football |
| 3        | WAR      |
| 2        | Vaccine  |
+----------+----------+
Posts 表:
+---------+------------------------------------------------------------------------+
| post_id | content                                                                |
+---------+------------------------------------------------------------------------+
| 1       | We call it soccer They call it football hahaha                         |
| 2       | Americans prefer basketball while Europeans love handball and football |
| 3       | stop the war and play handball                                         |
| 4       | warning I planted some flowers this morning and then got vaccinated    |
+---------+------------------------------------------------------------------------+
输出: 
+---------+------------+
| post_id | topic      |
+---------+------------+
| 1       | 1          |
| 2       | 1          |
| 3       | 1,3        |
| 4       | Ambiguous! |
+---------+------------+
解释: 
1: "We call it soccer They call it football hahaha"
"football" 表示主题 1。没有其他词能表示任何其他主题。

2: "Americans prefer basketball while Europeans love handball and football"
"handball" 表示主题 1。"football" 表示主题 1。
没有其他词能表示任何其他主题。

3: "stop the war and play handball"
"war" 表示主题 3。 "handball" 表示主题 1。
没有其他词能表示任何其他主题。

4: "warning I planted some flowers this morning and then got vaccinated"
这个句子里没有一个词能表示任何主题。注意 “warning” 和 “war” 不同，尽管它们有一个共同的前缀。
所以这篇文章 “Ambiguous!”
请注意，可以使用一个词来表达多个主题。



select post_id,ifnull(group_concat(distinct topic_id),'Ambiguous!') as topic
from posts
left join keywords
on instr(concat(' ',content,' '),concat(' ',word,' '))>0
group by post_id

# instr(totalSTR, findstr) --> totalSTR index from 1 to length(totalSTR)
