## chapter10

脚本守护进程化

```shell
nohup mydaemonscript 0<&-1>/dev/null 2>&1 &
或者
nohup mydamenoscript >> /var/log/myadmin.log 3>&1 <&- &
```

代码重用

```shell
 $ cat mprefs.cfg
SCRATCH_DIR=/var/tmp
IMG_FMT=png
SND_FMT=ogg

$ source mprefs.cfg
$ echo $IMG_FMT
 png
$ cd ${SCRATCH_DIR:-/tmp}
/var/tmp  $
/var/tmp  $ ls
kernel_panics
/var/tmp  $ echo you prefer $IMG_FMT image files
you prefer png image files
/var/tmp  $ echo you prefer $SND_FMT sound files
you prefer ogg sound files
```

定义函数

```shell
$ cat myfunc.sh
function usage () {
    printf "usage: %s [ -a | -b ] file1 .....filen\n" ${0##*/} > &2
}

if [ $# -lt 1 ]
then
    usage
fi
# 函数样式
$ cat func_sample.sh
function usage ()
{
    printf "usage: %s [ -a | -b ] file1 .... filen\n" ${0##*/} > &2
}

function usage {
    printf "usage: %s [ -a | -b ] file1 .... filen\n" ${0##*/} > &2
}

usage ()
{
    printf "usage: %s [ -a | -b ] file1 .... filen\n" ${0##*/} > &2
}
```

