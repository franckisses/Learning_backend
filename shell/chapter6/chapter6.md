### chapter6

条件分支

```shell
$ cat trythis.sh
if ls; pwd; cd $1 ;
then
    echo success
else
    echo failed
fi
pwd

$ sh trythis.sh /Users
if.sh		trythis.sh
/Users/gongyan/Project/liangpi/shell/chapter6
success
/Users
~/Project/liangpi/shell/chapter6  ‹master*› $ sh trythis.sh /tmp
if.sh		trythis.sh
/Users/gongyan/Project/liangpi/shell/chapter6
success
/tmp
~/Project/liangpi/shell/chapter6  ‹master*› $ sh trythis.sh /noneexistsent
if.sh		trythis.sh
/Users/gongyan/Project/liangpi/shell/chapter6
trythis.sh: line 1: cd: /noneexistsent: No such file or directory
failed
/Users/gongyan/Project/liangpi/shell/chapter6
```

测试文件特性

```shell
$ cat checkfile
#!/usr/bin/env bash
# cookbook filename: checkfile
#
DIRPLACE=/tmp
INFILE=/Users/gongyan/Project/liangpi/shell/chapter6
OUTFILE=/Users/gongyan/Project/liangpi/shell/chapter6

if [ -d "$DIRPLACE" ]
then
    cd $DIRPLACE
    if [ -e "$INFILE" ]
    then
        if [ -w "$OUTFILE" ]
        then
            doscience < "$INFILE" >> "$OUTFILE"
        else
            echo "cannot write to $OUTFILE"
        fi
    else
        echo "cannot read from $INFILE"
    fi
else
    echo "cannot cd into $DIRPLACE"
fi
```

测试字符串特性

```shell
 $ cat checkstr.sh
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
----- 
$ sh checkstr.sh test123
has text
has text
$ sh checkstr.sh
zero length
zero length
```

测试等量关系

数值比较实用 -eq

如果字符串比价则是实用 =/==

```shell
 $ cat strvsnum.sh
#!/usr/bin/env bash
# cookbook filename: strvsnum
#
# the old string vs. numeric comparison dilemma
#
VAR1=" 05 "
VAR2="5"

printf "%s" "do they -eq as equal? "
if [ "$VAR1" -eq "$VAR2" ]
then
    echo YES
else
    echo NO
fi

printf "%s" "do they = as equal? "
if [ "$VAR1" = "$VAR2" ]
then
    echo YES
else
    echo NO
fi
-----
$ sh strvsnum.sh
do they -eq as equal? YES
do they = as equal? NO
```

用模式匹配进行测试

```shell
 $ cat match.sh
shopt -s extglob
if [[ "test.jpg" == *.@(jpeg|jpg) ]]
then
    echo "Have one times"
else
    echo "have not find"
fi
```

| 拓展模式  | 含义                   |
| --------- | ---------------------- |
| @(.....)  | 仅匹配一次             |
| *(......) | 匹配0次和无数次        |
| +(....)   | 匹配一次或者多次       |
| ?(....)   | 匹配0次或者1次         |
| !(.....)  | 匹配除此之外的任何模式 |

循环若干次

````shell
for (( i=0 ; i < 10 ; i++)) ; do ehco $i; done

for i in 1 2 3 4 5 6 7 8 9 10
do 
    echo $i
done

seq 1.0 .01 1.1| # seq 可以生成连续的浮点数 1start .01 step 1.1 end
while read fp
do 
   echo $fp
done
````

解析命令行参数

```shell
$ cat dashes.sh
#!/usr/bin/env bash
# cookbook filename: dashes
#
# dashes - print a line of dashes
#
# options: # how many (default 72)
# -c X use char X instead of dashes
#

LEN=72
CHAR='-'
while (( $# > 0 ))
do
    case $1 in
        [0-9]*) LEN=$1
        ;;
        -c) shift;
               CHAR=${1:--}
        ;;
        *) printf 'usage: %s [-c X] [#]\n' ${0##*/} >&2
            exit 2
        ;;
    esac
    shift
done
```

创建简单的菜单

dbinit.1

```shell

$ cat dbinit.1                                        
#!/usr/bin/env bash
# cookbook filename: dbinit.1
#
DBLIST=$(sh ./listdb | tail -n +2)
select DB in $DBLIST
do
    echo Initializing database: $DB
    mysql -u user -p $DB <myinit.sql
done
```

dbinit.2

```shell
$ cat dbinit.2
#!/usr/bin/env bash
# cookbook filename: dbinit.2
#
DBLIST=$(sh ./listdb | tail -n +2)

PS3="0 inits >"

select DB in $DBLIST
do
    if [ $DB ]
    then
        echo Initializing database: $DB

        PS3="$((++i)) inits> "

        mysql -u user -p $DB <myinit.sql
    fi
done
```













