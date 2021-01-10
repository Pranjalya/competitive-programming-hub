# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        i = 1
        n = self.count(head)

        if n < k:
            return head
        if 2*k-1 == n:
            return head

        i = head
        i_p = ListNode()
        for _ in range(k-1):
            i_p = i
            i = i.next

        j = head
        j_p = ListNode()
        for _ in range(n - k):
            j_p = j
            j = j.next

        if i_p is not None:
            i_p.next = j

        if j_p is not None:
            j_p.next = i

        i.next, j.next = j.next, i.next

        if k == n:
            head = i
        if k == 1:
            head = j
        return head

    def count(self, head: ListNode) -> int:
        count = 1
        node = head
        while node.next is not None:
            count += 1
            node = node.next
        return count
