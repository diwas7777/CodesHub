package main

import "fmt"

func BubbleSort(array []int, l int) []int {
	for i := 0; i < l-1; i++ {
		for j := 0; j < l-i-1; j++ {
			if array[j] > array[j+1] {
				array[j], array[j+1] = array[j+1], array[j]
			}
		}
	}
	return array
}
func main() {
	array := []int{11, 40, 3, 38, 18, 70, 43}
	l := len(array)
	fmt.Println(BubbleSort(array, l))
}
