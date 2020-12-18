package subsequence

import "math"

func increasingTriplet(nums []int) bool {
	if len(nums) < 3 {
		return false
	}

	min1 := math.MaxInt32
	min2 := math.MaxInt32

	for _, v := range nums {
		if v < min1 {
			min1 = v
		}
		if v < min2 && v > min1 {
			min2 = v
		}
		if v > min2 {
			return true
		}
	}
	return false
}
