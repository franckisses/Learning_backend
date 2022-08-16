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
