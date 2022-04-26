package main

import "fmt"

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	initColor := image[sr][sc]
	if initColor == newColor {
		return image
	}
	nr, nc := len(image), len(image[0])
	wq := [][]int{}
	wq = append(wq, []int{sr, sc})

	directions := [4][2]int{
		{-1, 0}, {1, 0}, {0, -1}, {0, 1},
	}
	image[sr][sc] = newColor
	for i := 0; i < len(wq); i++ {
		fmt.Println(wq)
		// 把当前元素上下左右符合条件的像素加入 wq
		for _, direction := range directions {
			dr := wq[i][0] + direction[0]
			dc := wq[i][1] + direction[1]
			// 判断是否是存在的元素
			if dr >= 0 && dc >= 0 && dr < nr && dc < nc {
				if image[dr][dc] == initColor {
					if image[dr][dc] != newColor {
						image[dr][dc] = newColor
					}
					wq = append(wq, []int{dr, dc})
				}
			}
		}

	}

	return image
}

func main() {
	image := [][]int{{0,0,0}, {0, 1, 1}}
	floodFill(image, 1, 1, 1)
	fmt.Print(&image)
}
