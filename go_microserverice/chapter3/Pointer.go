package main 

import "fmt"

func main() {
    //声明一个string 类型
    str := "Golang is Good!"
    strPrt := &str
    
    fmt.Printf("str type is %T, and value is %v\n", str, str)
    fmt.Printf("strPrt type is %T, and value is %v\n", strPrt, strPrt)
}

/* 
go语言中，指针包含以下三个概念
 指针地址
 指针类型
 指针取值

 如果一个变量类型为T. 可以通过取址符号&获取该变量对应内存的地址
 生成该变量的指针，此时变量的内存地址即生成的指针的址。

 指针类型为*T,称为T的指针类型， “*”代表指针
 */
