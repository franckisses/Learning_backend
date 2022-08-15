#!/usr/bin/env base
# 实例文件
# 
# 找出文件大小
# 使用数组将ls -l 的输出解析成多个单词

LSL=$(ls -l $1)
declare -a MYRA
MYRA=($LSL)
echo the file $1 is ${MYRA[4]} bytes
