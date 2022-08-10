## chapter10

脚本守护进程化

```shell
nohup mydaemonscript 0<&-1>/dev/null 2>&1 &
或者
nohup mydamenoscript >> /var/log/myadmin.log 3>&1 <&- &
```

