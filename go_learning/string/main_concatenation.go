package main

import (  
    "fmt"
)

func main() {  
    string1 := "Go"
    string2 := "is awesome"
    result := string1 + " " + string2
    fmt.Println(result)


	result2 := fmt.Sprintf("%s %s", string1, string2)
    fmt.Println(result2)
}