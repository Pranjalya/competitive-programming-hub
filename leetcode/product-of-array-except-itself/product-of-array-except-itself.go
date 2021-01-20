package productofarrayexceptitself

func productExceptSelf(nums []int) []int {
	var n int = len(nums) - 1
	var left, right int = 1, 1
	var ans []int = make([]int, n+1)
	for i := range ans {
		ans[i] = 1
	}
	for i := range nums {
		ans[i] *= left
		ans[n-i] *= right
		left *= nums[i]
		right *= nums[n-i]
	}
	return ans
}
