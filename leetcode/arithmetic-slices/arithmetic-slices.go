package arithmeticslices

func numberOfArithmeticSlices(A []int) int {
	i := 2
	ans := 0
	for k := 0; k < len(A)-2; k++ {
		if A[k+1]-A[k] == A[k+2]-A[k+1] {
			ans += i - 1
			i++
		} else {
			i = 2
		}
	}
	return ans
}
