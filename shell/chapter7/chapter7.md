## chapter7

在文件中查找字符串

```shell
grep find_str file
$ grep 119 sshlogin.sh
  $ ssh 119.22.2.100 xxx xxx_123
# 在多个文件中查找
$ grep echo *.sh
checkstr.sh:    echo has text
checkstr.sh:    echo zero length
checkstr.sh:    echo zero length
checkstr.sh:    echo has text
match.sh:    echo "Have one times"
match.sh:    echo "have not find"
strvsnum.sh:    echo YES
strvsnum.sh:    echo NO
strvsnum.sh:    echo YES
strvsnum.sh:    echo NO
trythis.sh:    echo success
trythis.sh:    echo failed
```

只显示包含搜索结果的文件名

```shell
$ grep -l echo *.sh
checkstr.sh
match.sh
strvsnum.sh
trythis.sh

--删除包含结果的文件
rm -i $(grep -l 'this is test' *)
```

了解是否搜索成功

```shell
$ if grep -q 'test' if.sh; then echo yes ; else echo nope; fi
nope

$ cat if.sh
if list; then list; [elif list; then list;] ... [ else  list] fi

$ if grep -q 'else' if.sh; then echo yes ; else echo nope; fi
yes

$ if grep 'else' if.sh > /dev/null; then echo yes; else echo nope; fi
```

不区分大小写搜索

```shell
$ cat logfile.msgs
error
Error
ERROR
eRroR

$ grep -i error logfile.msgs
error
Error
ERROR
eRroR
```

保留部分输出

```shell
$ ls -l
total 16
-rw-r--r--@ 1 gongyan  staff  1197  8  7 21:46 chapter7.md
-rw-r--r--  1 gongyan  staff    24  8  7 21:39 logfile.msgs
$ ls -l |awk '{print $1}'
total
-rw-r--r--@
-rw-r--r--
```

保留部分输入行

```shell
$ ls -l |awk '{print $1, $NF}'
total 16
-rw-r--r--@ chapter7.md
-rw-r--r-- logfile.msgs
# NF 是awk的内建变量.是当前行中的字段总数，$NF 是总是引用最后一个字段
```

用awk统计字符串出现的次数

```shell
$ cat asar.awk

#!/usr/bin/awk -f
# cookbook filename: asar.awk
# Associative arrays in Awk
# Usage: ls -lR /usr/local | asar.awk

NF > 7 {
    user[$3]++
}
END {
    for (i in user) {
        printf "%s owns %d files\n", i, user[i]
    }
}

$ ls -lR /usr/local |awk -f  asar.awk
nobody owns 5 files
root owns 22402 files
_mysql owns 32 files
gongyan owns 57207 files
```

用便捷直方图展示数据

```shell
$ cat hist.awk
#!/usr/bin/awk -f
# cookbook filename: hist.awk
# Histograms in Awk
# Usage: ls -lR /usr/local | hist.awk

function max(arr, big)
{
    big = 0;
    for (i in user)
    {
        if (user[i] > big) { big=user[i];}
    }
    return big
}

NF > 7 {
    user[$3]++
}
END {
    # for scaling
    maxm = max(user);
    for (i in user) {
        #printf "%s owns %d files\n", i, user[i]
        scaled = 60 * user[i] / maxm ;
        printf "%-10.10s [%8d]:", i, user[i]
        for (i=0; i<scaled; i++) {
            printf "#";
        }
        printf "\n";
    }
}
$ ls -lR /usr/local |awk -f  asar.awk
 nobody     [       5]:#
root       [   22402]:########################
_mysql     [      32]:#
gongyan    [   57207]:############################################################
```





















