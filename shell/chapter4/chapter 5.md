## chapter 5

了解命令是否运行成功 

```shell
echo $?
0 运行成功
非0 运行失败
```

将命令压到后台执行，在命令后面加上&

```shell
sh test.sh &
nohup sh test.sh & # 无人值守下运行耗时作业
```

当一个命令运行成功后，在运行下一个命令

```shell
cd mytest
if (( $? == 0 )); then rm * ; fi
# 或者
if cd mytest; then rm *; fi 

# 或者
cd mytest && rm *
```

出现故障时显示调试信息

```shell
a && b # 如果a 执行成功，再执行b  a and b 
cd mytest && rm *
a || b # 如果a 执行成功，则不用执行b a or b 
cd mytest || printf "%b" "cnd failed, you're on your own\n"
```

执行变量中的命令. var_cmd.sh

```shell
FN=/Users/gongyan/Project/liangpi/shell/chapter5/abc.txt
PROG=echo
$PROG $FN
PROG=cat 
$PROG $FN
```



