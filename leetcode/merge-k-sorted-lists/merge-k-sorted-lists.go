package mergeksortedlists

import "math"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeKLists(lists []*ListNode) *ListNode {
	var index, min int
	index, min = -1, math.MaxInt32
	for i, node := range lists {
		if node != nil && node.Val < min {
			index = i
			min = node.Val
		}
	}
	if index == -1 {
		return nil
	}
	head := lists[index]
	lists[index] = lists[index].Next
	head.Next = mergeKLists(lists)
	return head
}
