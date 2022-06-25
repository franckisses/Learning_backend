## Autovacuum

### 什么是autovacuum

autovacuum 是启动PostgreSQL时自动启动后台实用程序进程之一,在生产系统中不应该将其设置为关闭；

```ini
autovacuum = on # on by default
track_counts = on # on by default 
```

### 为什么需要autovacuum

 需要使用vacuum 来移除死元祖。删除的内容来释放内存；

 防止死元祖膨胀；

更新表的统计信息进行分析，以便提供优化器使用

autovacuum launcher 使用stats collector的后台进程收集的信息来确定；