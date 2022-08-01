#!/usr/bin/env bash

for FN in $*
do
    echo changing $FN
    chmod 777 $FN
done
