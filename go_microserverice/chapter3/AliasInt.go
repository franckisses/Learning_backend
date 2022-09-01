package main 

import "fmt"

type aliasInt = int // 定义一个类型别名
type myInt int // 定义一个新的类型


func main() {
    var alias aliasInt
    fmt.Printf("alias value is %v, type is %T\n", alias, alias)

    var myint myInt
    fmt.Printf("alias value is %v, type is %T\n", myint, myint)

    //根据人名分配工作
    name := "小红" 
    switch name {
    case "小明":
        fmt.Printf("扫地")
    case "小红":
        fmt.Printf("擦黑板")
    case "小刚":
        fmt.Printf("倒垃圾")
    default:
	fmt.Printf("都他么歇着吧")
    }

    // 根据分数判断成绩等级
    score := 90
    switch {
	case score < 100 && score >= 90:
	   fmt.Printf("A")
        case score < 90 && score >= 80:
           fmt.Printf("B")
	case score < 80 && score >= 60:
	   fmt.Printf("C")
        case score < 60:
	   fmt.Printf("D")
	default:
	   fmt.Printf("Error")
	}
}

// 对于变量运行是的特点，常量的值在声明之后不允许变化，
// 通过const 关键字可以声明常量
