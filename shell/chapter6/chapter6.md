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













