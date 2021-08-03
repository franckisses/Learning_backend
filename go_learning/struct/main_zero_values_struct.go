package main

import (  
    "fmt"
)

type Employee struct {  
    firstName string
    lastName  string
    age       int
    salary    int
}

func main() {  
    var emp4 Employee //zero valued struct
    fmt.Println("First Name:", emp4.firstName)
    fmt.Println("Last Name:", emp4.lastName)
    fmt.Println("Age:", emp4.age)
    fmt.Println("Salary:", emp4.salary)
}