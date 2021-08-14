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


func (u *user) notify() {
	fmt.Printf("sending user email to %s:<%s>\n",u.name,u.email)
}

type admin struct {
	user 
	level string 
}

func (a *admin) notify() {
	fmt.Printf("sending admin email to %s:<%s>\n",a.name,a.email)
}


func main() {
	ad 	:= admin {
		user : user {
			name: "john smith",
            email: "john@yahoo.com",
		},
		level :"super",
	} 
	
	sendNotification(&ad)

	ad.user.notify()

	ad.notify()
}

func sendNotification(n notifier) {
	n.notify()
}
