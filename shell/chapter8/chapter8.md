## chapter8

输出排序

sort 按照文件大小排序

```shell
$ ls -l|sort
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 amazing.data
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 more.results
-rw-r--r--  1 gongyan  staff    68  8  5 22:38 if.sh
-rw-r--r--  1 gongyan  staff    71  8  5 22:40 trythis.sh
-rw-r--r--  1 gongyan  staff    83  8  6 21:56 listdb
-rw-r--r--  1 gongyan  staff   119  8  6 21:30 match.sh
-rw-r--r--  1 gongyan  staff   189  8  6 21:46 dbinit.1
-rw-r--r--  1 gongyan  staff   222  8  6 22:04 func_clac
-rw-r--r--  1 gongyan  staff   279  8  6 21:47 dbinit.2
-rw-r--r--  1 gongyan  staff   325  8  6 21:16 strvsnum.sh
-rw-r--r--  1 gongyan  staff   371  8  6 21:11 checkstr.sh
-rw-r--r--  1 gongyan  staff   416  8  6 21:42 dashes.sh
-rw-r--r--  1 gongyan  staff   519  8  6 22:00 rpncalc
-rw-r--r--  1 gongyan  staff   537  8  6 20:48 checkfile
-rw-r--r--@ 1 gongyan  staff  4061  8  6 22:06 chapter6.md
total 104
$ ls -l|sort -r # 逆序。从大到小
total 104
-rw-r--r--@ 1 gongyan  staff  4061  8  6 22:06 chapter6.md
-rw-r--r--  1 gongyan  staff   537  8  6 20:48 checkfile
-rw-r--r--  1 gongyan  staff   519  8  6 22:00 rpncalc
-rw-r--r--  1 gongyan  staff   416  8  6 21:42 dashes.sh
-rw-r--r--  1 gongyan  staff   371  8  6 21:11 checkstr.sh
-rw-r--r--  1 gongyan  staff   325  8  6 21:16 strvsnum.sh
-rw-r--r--  1 gongyan  staff   279  8  6 21:47 dbinit.2
-rw-r--r--  1 gongyan  staff   222  8  6 22:04 func_clac
-rw-r--r--  1 gongyan  staff   189  8  6 21:46 dbinit.1
-rw-r--r--  1 gongyan  staff   119  8  6 21:30 match.sh
-rw-r--r--  1 gongyan  staff    83  8  6 21:56 listdb
-rw-r--r--  1 gongyan  staff    71  8  5 22:40 trythis.sh
-rw-r--r--  1 gongyan  staff    68  8  5 22:38 if.sh
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 more.results
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 amazing.data
$ ls -l|sort -f # 不区分大小写
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 amazing.data
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 more.results
-rw-r--r--  1 gongyan  staff    68  8  5 22:38 if.sh
-rw-r--r--  1 gongyan  staff    71  8  5 22:40 trythis.sh
-rw-r--r--  1 gongyan  staff    83  8  6 21:56 listdb
-rw-r--r--  1 gongyan  staff   119  8  6 21:30 match.sh
-rw-r--r--  1 gongyan  staff   189  8  6 21:46 dbinit.1
-rw-r--r--  1 gongyan  staff   222  8  6 22:04 func_clac
-rw-r--r--  1 gongyan  staff   279  8  6 21:47 dbinit.2
-rw-r--r--  1 gongyan  staff   325  8  6 21:16 strvsnum.sh
-rw-r--r--  1 gongyan  staff   371  8  6 21:11 checkstr.sh
-rw-r--r--  1 gongyan  staff   416  8  6 21:42 dashes.sh
-rw-r--r--  1 gongyan  staff   519  8  6 22:00 rpncalc
-rw-r--r--  1 gongyan  staff   537  8  6 20:48 checkfile
-rw-r--r--@ 1 gongyan  staff  4061  8  6 22:06 chapter6.md
total 104
```

IP地址排序

```shell
$ cat ipaddr.list
10.0.0.2
10.0.0.5
10.0.0.20
192.168.0.2
192.168.0.4
192.168.0.12
$ sort -t. -n +3.0 ipaddr.list # 按照最后一位排序
10.0.0.2
192.168.0.2
192.168.0.4
10.0.0.5
192.168.0.12
10.0.0.20
 $ sort -t . -k 1,1n -k 2.2n -k 3.3n -k 4.4n ipaddr.list # 按照整个IP地址排序
10.0.0.2
10.0.0.5
10.0.0.20
192.168.0.2
192.168.0.4
192.168.0.12
```

提取部分输出

```
$ ls -l
total 112
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 amazing.data
-rw-r--r--@ 1 gongyan  staff  4061  8  6 22:06 chapter6.md
-rw-r--r--  1 gongyan  staff   537  8  6 20:48 checkfile
-rw-r--r--  1 gongyan  staff   371  8  6 21:11 checkstr.sh
-rw-r--r--  1 gongyan  staff   416  8  6 21:42 dashes.sh
-rw-r--r--  1 gongyan  staff   189  8  6 21:46 dbinit.1
-rw-r--r--  1 gongyan  staff   279  8  6 21:47 dbinit.2
-rw-r--r--  1 gongyan  staff   222  8  6 22:04 func_clac
-rw-r--r--  1 gongyan  staff    68  8  5 22:38 if.sh
-rw-r--r--  1 gongyan  staff    65  8  8 22:07 ipaddr.list
-rw-r--r--  1 gongyan  staff    83  8  6 21:56 listdb
-rw-r--r--  1 gongyan  staff   119  8  6 21:30 match.sh
-rw-r--r--  1 gongyan  staff     0  8  6 20:48 more.results
-rw-r--r--  1 gongyan  staff   519  8  6 22:00 rpncalc
-rw-r--r--  1 gongyan  staff   325  8  6 21:16 strvsnum.sh
-rw-r--r--  1 gongyan  staff    71  8  5 22:40 trythis.sh
$ ls -l|cut -c1-10
total 112
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
-rw-r--r--
```

删除重复行

```shell
$ ls -l
total 24
-rw-r--r--@ 1 gongyan  staff  4329  8  8 22:16 chapter8.md
-rw-r--r--  1 gongyan  staff    65  8  8 22:07 ipaddr.list
$ ls -l|cut -c15-21

gongyan
gongyan
$ ls -l|cut -c15-21| uniq

gongyan
# 如果对输出的结果需要排序，则需要加上 -u 选项
```

统计文件的行数、单词数或字符数

```shell
 $ wc chapter8.md
     148     703    4664 chapter8.md
 $ wc -l chapter8.md # 统计行数
     151 chapter8.md
$ wc -w chapter8.md # 统计单词数
     710 chapter8.md
$ wc -c chapter8.md
    4721 chapter8.md # 统计字符数（字节数）
```

