package main

import "fmt"

func createCounter(initial int) func() int {
	fmt.Println("vim-go")
	if initial < 0 {
		initial = 0
	}
	return func() int {
		initial++
		return initial
	}
}

func main() {
	// 计数器 1
	c1 := createCounter(1)

	fmt.Println(c1()) //2
	fmt.Println(c1()) //3

	c2 := createCounter(10)
	fmt.Println(c2()) // 11
	fmt.Println(c1()) //4

}
