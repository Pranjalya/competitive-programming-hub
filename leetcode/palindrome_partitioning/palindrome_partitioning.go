package palindromepartitioning

func isAlphaNum(char byte) bool {
	return (char >= '0' && char <= '9') || (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z')
}

func isPalindrome(s string) bool {
	l := 0
	r := len(s) - 1
	for l < r {
		if !isAlphaNum(s[l]) {
			l++
			continue
		}
		if !isAlphaNum(s[r]) {
			r--
			continue
		}
		if s[l] == s[r] {
			l++
			r--
		} else {
			return false
		}
	}
	return true
}

func update(s string, path []string, result [][]string) [][]string {
	if len(s) == 0 {
		result = append(result, path)
		return result
	}
	for i := 0; i < len(s); i++ {
		if isPalindrome(s[:i+1]) {
			result = update(s[i+1:], append(path, s[:i+1]), result)
		}
	}
	return result
}

func partition(s string) [][]string {
	var result [][]string
	var path []string
	return update(s, path, result)
}
