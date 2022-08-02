#!/usr/bin/env bash 

#实例文件 check_arg_count

#检查参数数量
#使用下列语法 if [ $# -lt 3 ]

if (( $# < 3 )) 
then 
    printf "%b" "Error. not enough arguement.\n" >&2 
    printf "%b" "usage: myscript file1 op file2\n" >&2
    exit 1
elif (( $# > 3 ))
then 
    printf "%b" "Error. not enough arguement.\n" >&2
    printf "%b" "usage: myscript file1 op file2\n" >&2
    exit 2
else
    printf "%b" "Argument count correct. Proceeding... \n"
fi
