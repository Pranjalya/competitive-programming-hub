package longestpalindrome

func updateValues(s string, low, high, maxl, start int) (int, int, int, int) {
	for low >= 0 && high < len(s) && s[low] == s[high] {
		if high-low+1 > maxl {
			start = low
			maxl = high - low + 1
		}
		low--
		high++
	}
	return low, high, start, maxl
}

func longestPalindrome(s string) string {
	maxl := 1
	start := 0
	length := len(s)
	low := 0
	high := 0

	for i := 1; i < length; i++ {
		low = i - 1
		high = i
		low, high, start, maxl = updateValues(s, low, high, maxl, start)
		low = i - 1
		high = i + 1
		low, high, start, maxl = updateValues(s, low, high, maxl, start)
	}

	return s[start : start+maxl]
}
