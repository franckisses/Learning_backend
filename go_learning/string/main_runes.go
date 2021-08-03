package main

import (  
    "fmt"
)

func charsAndBytePosition(s string) {  
    for index, rune := range s {
        fmt.Printf("%c starts at byte %d\n", rune, index)
    }
}

func main() {  
    name := "Señor"
    charsAndBytePosition(name)
}