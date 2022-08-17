#########################################################################
# File Name:   
# Author:       Franckisses 
# Mail:         franckisses@gmail.com
# Created Time: 2022-08-17
#########################################################################
#!/usr/bin/env bash
# 通过标准文件初始化数据库

DBLIST=$(mysql -e "SHOW DATABASES;" | tail -n +2)
select DB in $DBLIST "new..."
do
    if [[ $DB == "new..." ]]
    then
        printf "%b" "name for new db: "
        read DB rest
        echo creating new database $DB
        mysql -e "CREATE DATABASE IF NOT EXISTS $DB;"
    fi

    if [ -n "$DB" ]
    then
        echo Initializing database: $DB
        mysql $DB < ourInit.sql
    fi
done
