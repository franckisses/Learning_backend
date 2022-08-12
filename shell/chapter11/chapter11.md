格式化日期显示

```shell
 $ cat date.sh
STRICT_ISO_8601='%Y-%m-%dT%H:%M:%S%z'
ISO_8601='%Y-%m-%d %H:%M:%S %Z'
ISO_8601_1='%Y-%m-%d %T %Z'
DATEFILE='%Y%m%d%H%M%S'

echo $(date "+$ISO_8601")

# awk "BEGIN {print strfime(\"$ISO_8601\")}"

echo $(date '+%Y-%m-%d %T %Z')

# echo $(date -d '2022-08-12' "+$ISO_8601")

echo $(date "+Program Starting at: $ISO_8601")

printf "%b" "Program starting at: $(date '+$ISO_8601')\n"

echo "i can rename a file like this : mv file.log file_$(date +$DATEFILE).log"
$ sh date.sh  
2022-08-12 17:37:31 EET
2022-08-12 17:37:31 EET
Program Starting at: 2022-08-12 17:37:31 EET
Program starting at: $ISO_8601
i can rename a file like this : mv file.log file_20220812173731.log
```

时间戳

```shell
$ date "+%s"
1660319124
```

