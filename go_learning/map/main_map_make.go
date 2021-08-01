package main

import (  
    "fmt"
)

func main() {  
    employeeSalary := make(map[string]int)
	// add items
	employeeSalary["steve"] = 12000
    employeeSalary["jamie"] = 15000
    employeeSalary["mike"] = 9000
    fmt.Println("employeeSalary map contents:", employeeSalary)

	// by declaration 
	employeeSalary1 := map[string]int {
        "steve": 12000,
        "jamie": 15000,
    }
    employeeSalary1["mike"] = 9000
    fmt.Println("employeeSalary1 map contents:", employeeSalary1)

	employee := "jamie"
    salary := employeeSalary[employee]
    fmt.Println("Salary of", employee, "is", salary)


	// check exists or not 
	newEmp := "joe"
    value, ok := employeeSalary[newEmp]
    if ok == true {
        fmt.Println("Salary of", newEmp, "is", value)
        return
    }
    fmt.Println(newEmp, "not found")

	// iteratble 
	fmt.Println("Contents of the map")
    for key, value := range employeeSalary {
        fmt.Printf("employeeSalary[%s] = %d\n", key, value)
    }

	// delete items from the map
	fmt.Println("map before deletion", employeeSalary)
    delete(employeeSalary, "steve")
    fmt.Println("map after deletion", employeeSalary)

}