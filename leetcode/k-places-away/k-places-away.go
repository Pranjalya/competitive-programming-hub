package kplacesaway

func kLengthApart(nums []int, k int) bool {
	if k == 0 {
		return true
	}
	var first bool = true
	var prev int
	for i, v := range nums {
		if v == 1 {
			if first {
				first = false
				prev = i
				continue
			}
			if i-prev <= k {
				return false
			}
			prev = i
		}
	}
	return true
}
