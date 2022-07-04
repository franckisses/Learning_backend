### PostgreSQL 单表查询成本估算算法

sql语句执行五步骤

1. 解析器[parser] 解析器从纯文本的sql语句生成解析树
2. 分析仪/分析器[analyzer/analyser] 对解析树执行语义分许并生成查询树
3. 重写器[rewriter] 使用存储在规则系统中的规则，转为查询树
4. 规划器[planner] 计划者从出阿寻书生成可以最有效的执行计划树。
5. 执行器[executor] 通过按照计划树创建的顺序访问表和索引来执行查询。



### 单表查询中成本估算

 优化基于成本，成本是无量纲值，不是绝对绩效指标，

执行器执行的所有操作都具有响应的成本函数

三种成本： 启动，运行，总计，总成本是启动和运行成本的总和。

启动成本是获取第一个行之前花费的成本，例如 索引扫描节点的启动，成本就是读取索引页面以访问目标表中第一个元祖的成本

运行成本是获取所有行的成本

总成本就是启动和运行成本的成本之和。

### 单表查询成本估算之顺序扫描

Sequential Scan 成本计算

顺序扫描的成本由cost_seqsc() 函数估算。

```
testdb# select * from tbl where id < 8000;
```

在顺序扫描中，启动成本等于0，运行成本由以下等式定义：

```
= 'cpu run cost' + 'disk run cost'
= (cpu_tuple_cost + cpu_operator_cost) * N(tuple) + seq_page_cost * N(page)
```



\d pg_setting



select name.setting from pg_settings where name like 'cpu%';



查看数据表占用存储数据块

```
select relpages, reltuples from pg_class where relname='table_name';
```

### 单表查询成本估算之索引扫描

Index Scan 成本估算 启动成本估算公式

```
`start-up cost` = {ceil(log2(N index,tuple)) + (Hindex + 1) *50} X cpu_operator_cost
```

Hindex指的是索引的高度:

查询索引的行数和页数

```
select relpages,reltuple from pg_class where relname='tbl_data_idx';
-------+---------
  30   | 10000
```

#### 查询索引的高度

```
create extension pageinsspect;
sleect * from bt_metap('tbl_data_idx');
# level 即索引的高度
```

Index Scan成本估算

 运行成本计算公式， 索引扫描的运行成本是表和索引的CPU成本和IO(输入输出) 成本之和。
$$
run cost=（'index\; cpu\; cost + 'table\; cpu\; cost') + ('index\; IO\; cost' + 'table\; IO\; cost')
$$
前三个成本计算公式：
$$
Index cpu cost = Selectivity * N_{index,tuple} * (cpu\_index\_tuple\_cost + qual\_op\_cost)
$$

$$
table cpu cost = Selectivity * N_{tuple} * cpu_table_cost
$$

$$
Index IO cost = ceil(Selectivity * N_{index.page}) * random\_page\_cost
$$

### Selectivity

表的每一列的MCV(Most Common Value) 作为一堆most_common_vals和most_common_freqs的列存储在pg_stats试图中。

> ​	most_common_vals 是统计MCVs 列表的列
>
> ​    most_common_freqs 是统计mcv的频率列

```
select most_common_vals, most_common_freqs from pg_stats where tablename ='countries' and attname ='continent'

```





