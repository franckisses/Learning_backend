package main

import (  
    "fmt"
)


func main() {
	// 1   
    var a [3]int //int array with length 3
    a[0] = 12 // array index starts at 0
    a[1] = 78
    a[2] = 50
    fmt.Println(a)

	// 2 
	// a := [3]int{12, 78, 50} // short hand declaration to create array
    // fmt.Println(a)
	// [12 78 50]

	// 3
	// a := [3]int{12} 
    // fmt.Println(a) 

	// 4 
	a := [...]int{12, 78, 50} // ... makes the compiler determine the length
    fmt.Println(a)
}