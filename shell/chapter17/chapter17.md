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

将数据追加到文件开头

```shell
# shell 的方式
$ temp_file="temp.123"
$ (echo 'static header line1'; cat data_file) > $temp_file && cat $temp_file > data_file 
$ rm $temp_file 
$ unset temp_file

# sed 方式
$ cat data_file                                                    
1 foo
2 bar
3 baz
$ sed -e '1i\
quote> static header line1
quote> ' data_file
static header line1
1 foo
2 bar
3 baz

$ sed -e '1i\   
static header line1\
static header line2
' data_file
static header line1
static header line2
1 foo
2 bar
3 baz
$ cat header_file
Header line1
Header line2
$ sed -e '$r data_file' header_file
Header line1
Header line2
1 foo
2 bar
3 baz
```

文件比对

```shell
$ cat right            
record_1
record_2
record_4
record_5
record_6.differ
record_7
record_8
record_9.right only
record_10
$ cat left
record_1
record_2.left only
record_3
record_4
record_5.differ
record_6
record_7
record_8
record_9
record_10
$ comm -23 left right
record_2.left only
record_3
record_5.differ
record_6
record_9
record_10
$ comm -13 left right
record_2
record_5
record_6.differ
record_9.right only
record_10
$ comm -12 left right                                                  1 ↵
record_1
record_4
record_7
record_8
```
部分windows上开发的shell脚本无法在Linux 上面运行，此时可以使用dos2unix 命令来转换
```
dos2unix original_file
```

对行进行编号

```shell
$ cat -n right
     1	record_1
     2	record_2
     3	record_4
     4	record_5
     5	record_6.differ
     6	record_7
     7	record_8
     8	record_9.right only
     9	record_10
$ less -N right
$ nl right
     1	record_1
     2	record_2
     3	record_4
     4	record_5
     5	record_6.differ
     6	record_7
     7	record_8
     8	record_9.right only
     9	record_10
```

