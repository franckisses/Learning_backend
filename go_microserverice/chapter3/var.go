package main

import "fmt"

func main() {
    var a int = 100
    var b = "100"
    c := 0.17 // 使用：=段变量声明初始化时，左值中至少有一个变量必须是未定义过的变量
    fmt.Printf("a value is %v, Type is %T\n", a, a)
    fmt.Printf("a value is %v, Type is %T\n", b, b)
    fmt.Printf("a value is %v, Type is %T\n", c, c)

}
