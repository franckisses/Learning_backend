package main

import "fmt"

func main() {
	nums := [...]int{1, 2, 3, 4, 5, 6, 7, 8}
	// 数组的遍历
	for k, v := range nums {
		fmt.Println(k, v, " ")
	}

	fmt.Println()

	// 切片的遍历
	slis := []int{1, 2, 3, 4, 5, 6, 7, 8}
	for k, v := range slis {
		fmt.Println(k, v, "")
	}

	fmt.Println()

	tmpMap := map[int]string{
		0: "小明",
		1: "小红",
		2: "小张",
	}

	// 字典的遍历
	for k, v := range tmpMap {
		// k 为健值，v 为对应值
		fmt.Println(k, v, "")
	}
}
