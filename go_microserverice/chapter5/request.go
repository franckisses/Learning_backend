package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"strings"
)

func login(w http.ResponseWriter, r *http.Request) {
	fmt.Println("method:", r.Method) // 获取请求的方法

	if r.Method == "GET" {
		t, _ := template.ParseFiles("login.html")
		log.Println(t.Execute(w, nil))
	} else {
		// 请求的是登录数据，那么执行登录的逻辑判断
		_ = r.ParseForm()
		fmt.Println("username:", r.Form["username"])
		fmt.Println("password:", r.Form["password"])
		if pwd := r.Form.Get("password"); pwd == "123456" {
			// 验证密码是否正确
			fmt.Fprintf(w, "欢迎登录，hello, %s", r.Form.Get("username"))
		} else {
			fmt.Fprintf(w, "密码错误，请重新输入")
		}
	}
}

func sayHelloName(w http.ResponseWriter, r *http.Request) {
	_ = r.ParseForm()
	fmt.Println(r.Form)
	fmt.Println("path", r.URL.Path)
	for k, v := range r.Form {
		fmt.Println("key:", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprintf(w, "Hello, aoho") // 这个写入到w的输出到客户端的
}

func main() {
	http.HandleFunc("/", sayHelloName) // 设置访问的路由
	http.HandleFunc("/login", login)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("ListenAndServe:", err)
	}
	fmt.Println("vim-go")
}
