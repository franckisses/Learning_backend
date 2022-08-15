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

