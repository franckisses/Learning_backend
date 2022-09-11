package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

type User struct {
	Id       int
	Name     string
	Password string
}

var UserById = make(map[int]*User)
var UserByName = make(map[string][]*User)

func loginMemory(w http.ResponseWriter, r *http.Request) {
	fmt.Println("method:", r.Method)
	if r.Method == "GET" {
		t, _ := template.ParseFiles("login.html")
		log.Println(t.Execute(w, nil))
	} else {
		// 请求的是登录数据, 那么执行登录操作
		_ = r.ParseForm()
		fmt.Println("username:", r.Form["username"])
		fmt.Println("password:", r.Form["password"])
		user1 := User{1, r.Form.Get("username"), r.Form.Get("password")}
		store(user1)

		if pwd := r.Form.Get("password"); pwd == "123456" { // 验证密码是否正确
			fmt.Fprintf(w, "欢迎登录，Hello %s", r.Form.Get("username"))

		} else {
			fmt.Fprintf(w, "密码错误,请重新输入")
		}
	}
}

func store(user User) { // 存储用户信息
	UserById[user.Id] = &user
	UserByName[user.Name] = append(UserByName[user.Name], &user)

}

func userInfo(w http.ResponseWriter, r *http.Request) {
	fmt.Println(UserById[1])
	r.ParseForm()
	for _, user := range UserByName[r.Form.Get("username")] {
		fmt.Fprintf(w, " %v", user)
	}
}

func main() {
	http.HandleFunc("/login", loginMemory)
	http.HandleFunc("/info", userInfo)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("ListenAndServe:", nil)
	}
}
