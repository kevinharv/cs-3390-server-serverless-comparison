package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Print("Starting!\n")

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "Hello World!")
		fmt.Print("Request served!\n")
    })

    err := http.ListenAndServe(":8080", nil)

	if (err != nil) {
		fmt.Print(err)
	}
}