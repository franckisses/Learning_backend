package main

import (
	"fmt"
	"reflect"
)

// 定义一个人的借口
type Person interface {
	// 和人说话
	SayHello(name string)
	// 跑步
	Run() string
}

type Hero struct {
	Name  string
	Age   int
	Speed int
}

func (hero *Hero) SayHello(name string) {
	fmt.Println("hello "+name, ", I am"+hero.Name)
}

func (hero *Hero) Run() string {
	fmt.Println("I am running at speed", hero.Speed)
	return "Running"
}

func main() {
	typeOfHero := reflect.TypeOf(Hero{})
	fmt.Printf("Hero's type is %s, kind is %s\n", typeOfHero, typeOfHero.Kind())
	fmt.Println("vim-go")
	//fmt.Printf("*Hero's type is %s, kind is %s", reflect.TypeOf(&Hero{}), reflect.TypeOf(&Hero{}).Kind())

}
