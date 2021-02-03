# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = node = ListNode()
        while True:
            lists = [val for val in lists if val is not None]
            obj = min(lists, key=lambda x: x.val, default=None)
            if obj is None:
                break
            index = lists.index(obj)
            node.next = ListNode(obj.val)
            node = node.next
            lists[index] = lists[index].next
        return head.next
