package main

import (
    "flag"
    "fmt"
)

func main() {
    // 定义一个类型为String 名称为surname 的命令行参数
    // 参数依次是命令行的名称，默认值，提示
    surname := flag.String("surname", "王", "您的姓")
    // 定义一个类型为string,名称为personalName的命令行参数
    // 除了返回指针类型的结果，还可以直接传入变量地址获取参数值
    var personalName string
    flag.StringVar(&personalName, "personalName", "小二", "您的名")
    // 定义一个类型int ,名称为id的命令行参数
    id := flag.Int("id", 0, "您的id")
    // 解析命令行参数
    flag.Parse()
    fmt.Printf("i am %v %v, and my id is %v\n", *surname, personalName, *id)
}
