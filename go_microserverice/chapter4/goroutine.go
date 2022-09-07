package main

import (
	"fmt"
	"time"
)

func test() {
	fmt.Println(" i am work in a single  goroutine!")
}

func main() {
	go test()
	// 主goroutine 休眠 1 s
	time.Sleep(1)
	fmt.Println("vim-go")
}
