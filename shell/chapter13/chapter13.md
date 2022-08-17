将输出解析到数组

```shell
$ cat parseViaArray.sh
#!/usr/bin/env base
# 实例文件
#
# 找出文件大小
# 使用数组将ls -l 的输出解析成多个单词

LSL=$(ls -l $1)
declare -a MYRA
MYRA=($LSL)
echo the file $1 is ${MYRA[4]} bytes
$ sh parseViaArray.sh getops_sample.sh
the file getops_sample.sh is 545 bytes
```

用函数调用解析输出

```shell
$ cat parseViaFunc.sh
#!/usr/bin/env base
# 实例文件：parseViaFunc
#
# 通过函数调用解析ls -l 的输出
# ls -l 的输出类似与以下这样
# -rw-r--r--  1 gongyan  staff    0  8 13 23:32 chapter13.md

function lsparts ()
{
    PERMS=$1
    LCOUNT=$2
    OWNER=$3
    GROUP=$4
    SIZE=$5
    CRMONTH=$6
    CRDAY=$7
    CRTIME=$8
    FILE=$9
}

lsparts $(ls -l "$1")

echo $FILE HASE $LCOUNT 'link(s)' and is $SIZE bytes long.

$ sh parseViaFunc.sh parseViaArray.sh
parseViaArray.sh HASE 1 link(s) and is 195 bytes long.
```

用read语句解析文本

```shell
 $ cat readtest.sh

#!/usr/bin/env bash


read -a MYRAY

echo $MYRAY
echo $MYRAY[3]

 $ sh readtest.sh
we are the champions!
we
we[3]
```

读取整个文件

```shell
mapfile -t -s 1 -n 1500 -C showprg -c 100 BIGDATA < /tmp/myfile.data
-s 1 跳过第一行
-n 1500 读取到1500行
-c 100 每次读取100行

 $ cat readarray.sh

function showprg ()
{
    printf '.'
}

ls -l /usr/bin > /tmp/myfile.data

mapfile -t -s 1 -n 1500 -C showprg -c 100 BIGDATA < /tmp/myfile.data

echo


siz=${#BIGDATA[@]}
echo "size: ${siz}"
```

正确书写单词的复数

```shell
cat pluralize.sh
#!/usr/bin/env bash
# 实例文件 pluralize
# 如果$2的值不等于1或-1 则在单词的末尾加上s
# 该函数只会加s 算不上太聪明

function plural ()
{
    if [ $2 -eq q -o $2 -eq -1 ]
    then
        echo ${1}
    else
	echo ${1}s
    fi
}

while read num name
do
    echo $num $(plural "$name" $num)
done
```

一次提取一个字

```shell
$ cat onebyone.sh  
#########################################################################
# File Name:    onebyone.sh
# Author:       Franckisses
# Mail:         franckisses@gmail.com
# Created Time: 2022-08-17
#########################################################################
#!/bin/bash
# 从输入中一次解析 一个字符

while read ALINE
do
    for ((i=0; i < ${#ALINE}; i++))
    do
        ACHAR=${ALINE:i:1}
	echo $ACHAR
    done
done
$ sh onebyone.sh
test
t
e
s
t
nihao
n
i
h
a
o
women
w
o
m
e
n
```

通过标准文件初始化数据看

```shell
 $ cat dbiniter.sh
#########################################################################
# File Name:
# Author:       Franckisses
# Mail:         franckisses@gmail.com
# Created Time: 2022-08-17
#########################################################################
#!/usr/bin/env bash
# 通过标准文件初始化数据库

DBLIST=$(mysql -e "SHOW DATABASES;" | tail -n +2)
select DB in $DBLIST "new..."
do
    if [[ $DB == "new..." ]]
    then
        printf "%b" "name for new db: "
        read DB rest
        echo creating new database $DB
        mysql -e "CREATE DATABASE IF NOT EXISTS $DB;"
    fi

    if [ -n "$DB" ]
    then
        echo Initializing database: $DB
        mysql $DB < ourInit.sql
    fi
done
```

提取数据中特定字段

```shell
 $ sed -n '11,20p' /etc/passwd
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
_lp:*:26:26:Printing Services:/var/spool/cups:/usr/bin/false
_postfix:*:27:27:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
_scsd:*:31:31:Service Configuration Service:/var/empty:/usr/bin/false

 $ sed -n '11,20p' /etc/passwd | cut -d':' -f1,6,7
nobody:/var/empty:/usr/bin/false
root:/var/root:/bin/sh
daemon:/var/root:/usr/bin/false
_uucp:/var/spool/uucp:/usr/sbin/uucico
_taskgated:/var/empty:/usr/bin/false
_networkd:/var/networkd:/usr/bin/false
_installassistant:/var/empty:/usr/bin/false
_lp:/var/spool/cups:/usr/bin/false
_postfix:/var/spool/postfix:/usr/bin/false
_scsd:/var/empty:/usr/bin/false

```

更新数据文件中特定的字段

```shell
$ cat data_file
Line 1 ends
Line 2 ends
Line 3 ends
Line 4 ends
Line 5 ends
Line 6 ends
$ awk '{print $1,$2+5,$3}' data_file       
Line 6 ends
Line 7 ends
Line 8 ends
Line 9 ends
Line 10 ends
Line 11 ends
# 如果第二个字段中包含3，将其修改为8 并做标记
 $ awk '{if ($2 == "3") print $1, $2+5, $3, "Tweaked" ; else print $0;}' data_file
Line 1 ends
Line 2 ends
Line 8 ends Tweaked
Line 4 ends
Line 5 ends
Line 6 ends
```

