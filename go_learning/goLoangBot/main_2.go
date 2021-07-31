package main

import "fmt"

func main() {  
    //1
	var width, height int = 100, 50 //declaring multiple variables
	//2 
	var width, height = 100, 50 //"int" is dropped
    fmt.Println("width is", width, "height is", height)

	//3 
	var width, height int
    fmt.Println("width is", width, "height is", height)
    width = 100
    height = 50
    fmt.Println("new width is", width, "new height is", height)

	// 4 
	var (
        name   = "naveen"
        age    = 29
        height int
    )
    fmt.Println("my name is", name, ", age is", age, "and height is", height)
}