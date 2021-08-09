package main

import (
	"fmt"
)

type notifier interface {
	notify()
}

type user struct {
	name string
	email string 
}

type admin struct {
	name string 
	email string 
}

func (u *user) notify() {
	fmt.Printf("sending admin email to %s:<%s>\n",u.name,u.email)
}

func (a *admin) notify() {
	fmt.Printf("sending admin email to %s:<%s>\n",a.name,a.email)
}

func main() {
	bill := user{"Bill", "bill@email.com"}

	SendNotification(&bill)

	lisa := admin{"Lisa", "lisa@email.com"}
	SendNotification(&lisa)

}

func SendNotification(n notifier) {
	n.notify()
}