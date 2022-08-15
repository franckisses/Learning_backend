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

```
```

