设置安全的mask

​	文件的权限是 **666** 目录的权限是 **777**

```shell
bash-3.2$ touch umcurrent
bash-3.2$ ls -l
total 8
-rw-r--r--@ 1 gongyan  staff  21  8 18 20:44 chapter14.md
-rw-r--r--  1 gongyan  staff   0  8 19 21:34 umcurrent
bash-3.2$ umask 000; touch um_000
bash-3.2$ ls -lrth
total 8
-rw-r--r--@ 1 gongyan  staff    21B  8 18 20:44 chapter14.md
-rw-r--r--  1 gongyan  staff     0B  8 19 21:34 umcurrent
-rw-rw-rw-  1 gongyan  staff     0B  8 19 21:35 um_000
bash-3.2$ umask 022 ; touch um_022
bash-3.2$ ls -rlth
total 8
-rw-r--r--@ 1 gongyan  staff    21B  8 18 20:44 chapter14.md
-rw-r--r--  1 gongyan  staff     0B  8 19 21:34 umcurrent
-rw-rw-rw-  1 gongyan  staff     0B  8 19 21:35 um_000
-rw-r--r--  1 gongyan  staff     0B  8 19 21:35 um_022
bash-3.2$ umask 077; touch um_077
bash-3.2$ ls -rlrth
total 8
-rw-r--r--@ 1 gongyan  staff    21B  8 18 20:44 chapter14.md
-rw-r--r--  1 gongyan  staff     0B  8 19 21:34 umcurrent
-rw-rw-rw-  1 gongyan  staff     0B  8 19 21:35 um_000
-rw-r--r--  1 gongyan  staff     0B  8 19 21:35 um_022
-rw-------  1 gongyan  staff     0B  8 19 21:36 um_077
# 目录
bash-3.2$ umask 000; mkdir test
bash-3.2$ ls -l
total 8
-rw-r--r--@ 1 gongyan  staff  1124  8 19 21:37 chapter14.md
drwxrwxrwx  2 gongyan  staff    64  8 19 21:37 test
-rw-rw-rw-  1 gongyan  staff     0  8 19 21:35 um_000
-rw-r--r--  1 gongyan  staff     0  8 19 21:35 um_022
-rw-------  1 gongyan  staff     0  8 19 21:36 um_077
-rw-r--r--  1 gongyan  staff     0  8 19 21:34 umcurrent
```

在Path中查找人皆可写的目录

-L 测试符号链接

-d 确认目录存在

-l 获取目录的长格式

```shell
$ cat chkpath.sh                                                                 1 ↵
#!/usr/bin/env bash
# cookbook filename: chkpath.1
# Check your $PATH for world-writable or missing directories

exit_code=0

for dir in ${PATH//:/ }; do
    [ -L "$dir" ] && printf "%b" "symlink, "
    if [ ! -d "$dir" ]; then
        printf "%b" "missing\t\t"
          (( exit_code++ ))
    elif [ -n "$(ls -lLd $dir | grep '^d.......w. ')" ]; then
          printf "%b" "world writable\t"
          (( exit_code++ ))
    else
          printf "%b" "ok\t\t"
    fi
    printf "%b" "$dir\n"
done
exit $exit_code
$ sh chkpath.sh
ok		/Users/gongyan/.nvm/versions/node/v16.16.0/bin
ok		/Users/gongyan/anaconda3/bin
ok		/Users/gongyan/anaconda3/condabin
missing		/Library/Frameworks/Python.framework/Versions/3.6/bin
ok		/usr/local/bin
ok		/usr/local/bin
ok		/usr/bin
ok		/bin
ok		/usr/sbin
ok		/sbin
ok		/usr/local/go/bin
ok		/usr/local/mysql/bin
```

配置免密码登录 ssh/scp

```shell
# 使用此命令登录先生成公私钥
$ ssh-keygen -v -t rsa -b 4096 -C 'My tentcent Server key'
使用 scp 将公钥存放在 ～/.ssh/authorized_keys
$ scp ~/.ssh/id_das.pub user@ip:~/.ssh/authorzed_keys
# 然后就可以免密登录和免密传送文件
```

