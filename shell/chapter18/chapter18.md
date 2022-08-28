在任意目录之间切换

pushd

```
 $ pushd                                                                                    1 ↵
~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~/Project/liangpi ~
 $ pushd ~/Project/liangpi
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi ~/Project/liangpi/shell/chapter18 ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd
~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17 ~
$ pushd ~
~ ~/Project/liangpi/shell/chapter18 ~/Project/liangpi ~/Project/liangpi/shell ~/Project/liangpi/shell/chapter17
```

重复上一个命令

```shell
$ ls
chapter18.md
$ !!
$ ls
chapter18.md
$ !!
$ ls
chapter18.md
```

