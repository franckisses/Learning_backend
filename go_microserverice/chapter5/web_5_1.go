package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)

func sayHello(w http.ResponseWriter, r *http.Request) {
	_ = r.ParseForm()   //3 解析参数， 默认是不会解析的
	fmt.Println(r.Form) // 4 输出到服务器端打印信息
	fmt.Println("Path: ", r.URL.Path)
	fmt.Println("Host: ", r.Host)
	for k, v := range r.Form {
		fmt.Println("Key:", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	_, _ = fmt.Fprintf(w, "Hello, Web, %s", r.Form.Get("name")) // 写入w到客户端
}

func main() {
	http.HandleFunc("/", sayHello)           // 1 设置访问的路由
	err := http.ListenAndServe(":8080", nil) // 2 设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}
