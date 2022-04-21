package main

import "fmt"

func reverseWords(s string) string {
	res := []byte{}
	i, j, k := 0, 0, 0

	for j < len(s) {
		if s[j] == ' ' || j == len(s) - 1{
			k = j
			if s[j] == ' ' {
				k = j - 1
			}
			for k >= i {
				res = append(res, s[k])
				k--
			}
			fmt.Printf("res: %v\n", string(res))
			if string(s[j]) == " " {
				res = append(res, s[j])
			}
			i = j + 1
		}
		j++
	}
	return string(res)
}

func main() {
	s := "Let's take LeetCode contest"
	fmt.Print(reverseWords(s))
}