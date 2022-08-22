批量重命名文件

```shell
for FN in *.bad
do
    mv "$FN" "${FN%bad}bash"
done

for i in *.odt; do mv "$i" "$(echo "$i"|cut -d'=' -f1,3)"; done
```

批量解压zip文件

```shell
unzip '*.zip'

for x in /path/to/date*/name/*.zip; do unzip "$x"; done

for x in $(ls /path/to/date*/name/*.zip 2>/dev/null); do unzip $x; done
```

