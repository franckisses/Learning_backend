package main

import (  
    "fmt"
    "unicode/utf8"
)

func main() {  
    word1 := "Señor"
    fmt.Printf("String: %s\n", word1)
    fmt.Printf("Length: %d\n", utf8.RuneCountInString(word1))
    fmt.Printf("Number of bytes: %d\n", len(word1))

    fmt.Printf("\n")
    word2 := "Pets"
    fmt.Printf("String: %s\n", word2)
    fmt.Printf("Length: %d\n", utf8.RuneCountInString(word2))
    fmt.Printf("Number of bytes: %d\n", len(word2))
}