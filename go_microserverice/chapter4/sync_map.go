package main

import (
	"fmt"
	"strconv"
	"sync"
)

var syncMap sync.Map
var waitGroup sync.WaitGroup

func main() {
	routineSize := 5
	waitGroup.Add(routineSize)
	for i := 0; i < routineSize; i++ {
		go addNumber(i * 10)
	}

	// 开始等待

	waitGroup.Wait()
	var size int
	syncMap.Range(func(key, value interface{}) bool {
		size++
		fmt.Println("key-value pair is", key, value, " ")
		return true
	})
	fmt.Println("syncMap current size is " + strconv.Itoa(size))
	value, ok := syncMap.Load(0)
	if ok {
		fmt.Println("key 0 has value", value, " ")
	}
}

func addNumber(begin int) {
	for i := begin; i < begin+3; i++ {
		syncMap.Store(i, i)
	}
	waitGroup.Done()
}
