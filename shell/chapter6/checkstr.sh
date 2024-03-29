#!/usr/bin/env bash
# cookbook filename: checkstr
#
# if statement
# test a string to see if it has any length
#
# use the command-line argument
VAR="$1"
#
# if [ "$VAR" ] will usually work but is bad form, using -n is more clear
if [ -n "$VAR" ]
then
    echo has text
else
    echo zero length
fi
#
if [ -z "$VAR" ]
then
    echo zero length
else
    echo has text
fi

