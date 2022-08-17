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
