package main

import "fmt"

type Swimming struct {
}

func (swim *Swimming) swim() {
	fmt.Println("Swimming is my ability")
}

// 飞行特性
type Flying struct {
}

func (fly *Flying) fly() {
	fmt.Println("flying is my ability")
}

type WideDuck struct {
	Swimming
	Flying
}

type DomesticDuck struct {
	Swimming
}

func main() {
	// 声明一只野鸭，可以飞，也可以游泳
	wild := WideDuck{}
	wild.fly()
	wild.swim()

	// 声明一个家鸭只会游泳
	domestic := DomesticDuck{}
	domestic.swim()
	fmt.Println("vim-go")
}
