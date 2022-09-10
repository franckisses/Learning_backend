package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type User struct {
	Name   string
	Habits []string
}

func write(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application.json")
	w.Header().Set("X-Custom-Header", "custom") // 设置自定义头部
	w.WriteHeader(201)
	user := &User{
		Name:   "aoho",
		Habits: []string{"balls", "running", "hiking"},
	}
	json, _ := json.Marshal(user)
	w.Write(json)
}
func main() {
	http.HandleFunc("/write", write)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("ListenAndServe:", err)
	}
	fmt.Println("vim-go")
}
