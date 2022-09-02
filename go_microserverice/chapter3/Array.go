package main

import "fmt"

func main() {
    var classMates1 [3]string
    classMates1[0] = "小明"
    classMates1[1] = "小红"
    classMates1[2] = "小李" //通过下标为数组成员赋值
    fmt.Println(classMates1)
    fmt.Println("this is No.1 student is "+ classMates1[0]) //通过下标访问数组成员

    classmates2 :=[...]string{"小明", "小红", "小李"} //使用初始化列表初始化列表
    fmt.Println(classmates2)

    // 使用指针操作数组
    classMates3 := new([3]string)
    classMates3[0] = "小明"
    classMates3[1] = "小红"
    classMates3[2]= "小李"
    fmt.Println(*classMates3)
}
