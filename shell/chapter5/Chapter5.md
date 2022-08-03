## Chapter5

将变量名和周围的文本分隔开

```shell
# bad 
for FN in 1 2 3 4
do 
    touch re$FNport.txt
done

# good
for FN in 1 2 3 4 5
do
    touch rep${FN}port.txt
done
```

在shell脚本中使用参数

```shell 
simplest.sh 
echo $1

$ sh simplest.sh
$ sh simplest.sh
$ sh simplest.sh you see what i mean
you
$ sh simplest.sh one more time
one
# 如果多个数位，需要加上{} ，否则会被认为$1+0 例如
cat tricky.sh
echo $1 $10 ${10}
$ ./tricky.sh Ⅰ Ⅱ Ⅲ Ⅳ Ⅴ Ⅵ Ⅶ Ⅷ Ⅸ Ⅹ Ⅺ
Ⅰ Ⅰ0 X
```

遍历传入脚本的参数

```shell
#!/usr/bin/env bash

for FN in $*
do
    echo changing $FN
    chmod 777 $FN
done
$ sh chmod_all.l rep1port.txt rep2port.txt rep3port.txt
changing rep1port.txt
changing rep2port.txt
changing rep3port.txt
```

处理包含空格的参数

```shell
$ cat simple.sh
ls -l ${1}

$ sh simple.sh on my god
ls: on: No such file or directory
$ sh simple.sh "on my god"                                              
ls: god: No such file or directory
ls: my: No such file or directory
ls: on: No such file or directory

$ cat quoted.sh
ls -l "${1}"
$ sh quoted.sh "on my god"                          
-rw-r--r--  1 gongyan  staff  0  8  1 22:44 on my god
```

处理包含空格的参数列表

假如有如下文件名

vocals.mp3  

cool music.mp3

Tophit.mp3

在遍历的时候可以使用**$@**来接受参数，这样shell 就会认为是一个列表。而不会解析为字符串

```shell
echo "$@"
for FN in "$@"
do
    echo "$FN"
    chmod 777 "$FN"
done
```

统计参数数量

```shell
$ cat check_arg_count.sh   
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

$ sh check_arg_count.sh file1 op file2                        
Argument count correct. Proceeding...
$ sh check_arg_count.sh file1 op
Error. not enough arguement.
usage: myscript file1 op file2
$ sh check_arg_count.sh file1 op file2 file3                      
Error. not enough arguement.
usage: myscript file1 op file2
```

丢弃参数

```shell
$ cat use_up_option.sh
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
```

获取默认值

```shell
$ cat get_default.sh
FILEDIR=${1:-/tmp}
echo $FILEDIR

$ sh get_default.sh
/tmp
$ sh get_default.sh /Users/yangong
/Users/yangong
```

设置默认值

```shell
$ cat set_default.sh

echo $home
echo ${home:=/Users/gongyan}
echo $home
```

DIFF: :- 与 := ,:- 返回值。但不赋值。 := 执行赋值，并返回运算符右侧的值。

 对不存在消息输出错误消息

```shell
# cookbook filename: check_unset_parms
#
USAGE="usage: myscript scratchdir sourcefile conversion"
FILEDIR=${1:?"Error. You must supply a scratch directory."}
FILESRC=${2:?"Error. You must supply a source file."}
CVTTYPE=${3:?"Error. ${USAGE}"}
```

修改部分字符串

```shell
for FN in *.xlsx
do
    mv "$(pwd)/${FN}" "${FN%.xlsx}"
done
# 可以用于修改文件名
```

