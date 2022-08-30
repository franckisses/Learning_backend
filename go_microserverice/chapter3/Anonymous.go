package main

import "fmt"

func getName() (string, string){
    return "王", "小二"
}

func main() {
    surname,_ := getName()
    _,personalName := getName()
    fmt.Printf("My name is %v and my personal name is %v", surname, personalName)
}
