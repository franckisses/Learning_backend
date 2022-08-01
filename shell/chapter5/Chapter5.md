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

```

```

 