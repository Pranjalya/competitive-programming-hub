package boats

import "sort"

func numRescueBoats(people []int, limit int) int {
	count := 0
	sort.Ints(people)
	i, j := 0, len(people)-1
	for i <= j {
		if people[i]+people[j] <= limit {
			i++
		}
		j--
		count++
	}
	return count
}
