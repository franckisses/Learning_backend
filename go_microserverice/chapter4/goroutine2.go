package main

import (
	"fmt"
	"time"
)

func main() {
	go func(name string) {
		fmt.Println("hello " + name)
	}("xuan")
	// 主	goroutine 阻塞1s
	time.Sleep(1)
}
