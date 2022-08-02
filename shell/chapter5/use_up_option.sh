#!/usr/bin/env bash

# 使用丢弃一个选项
VERBOSE=0
if [[ $1 = -v ]]
then
    VERBOSE=1
    shift
fi 

for FN in "$@"
do 
    if (( VERBOSE == 1 ))
    then
        ehco changing $FN
    fi
    chmod 0750 "$FN"
done
