package main

import "C"
import "fmt"

//export printBye
func printBye() {
    fmt.Println("From DLL: Bye!")
}

//export sum
func sum(a int, b int) int {
    return a + b;
}

func main() {}
