package main

import (
	"log"
	"os"

	_ "github.com/goinaction/code/chapter2/sample/matchers" 
	"github.com/goinaction/code/chapter2/sample/search"
)

/*为了让 Go 语言对包做初始化操作，但是并不使用包里的标识符。为了让程序的 可读性更强，Go 编译器不允许声明导入某个包却不使用。下划线让编译器接受这类导入，并且 调用对应包内的所有代码文件里定义的 init 函数。
*/

// init is called prior to main.
func init() {
	// Change the device for logging to stdout.
	log.SetOutput(os.Stdout)
}

//main 的函数。 构建程序在构建可执行文件时，需要找到这个已经声明的 main 函数，把它作为程序的入口

func main() {
	// Perform the search for the specified term.
	search.Run("president")
}
