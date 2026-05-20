package main

import (
	"bytes"
	"fmt"
	"index/suffixarray"
	"io"
	"os"
)

func main() {
	inputBytes, err := io.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	
	data := bytes.TrimSpace(inputBytes)
	n := len(data)
	if n == 0 {
		return
	}

	sa := suffixarray.New(data)

	firstChar := data[0:1]
	suffixOffsets := sa.Lookup(firstChar, -1)

	longest := 0

	for _, offset := range suffixOffsets {
		if offset > 0 {
			length := n - offset
			
			if length <= longest {
				continue
			}

			if bytes.Equal(data[0:length], data[offset:]) {
				longest = length
			}
		}
	}

	fmt.Printf("Answer: %d\n", longest)
}