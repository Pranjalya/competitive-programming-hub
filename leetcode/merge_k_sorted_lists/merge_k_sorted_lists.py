# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insert(self, node, val):  
        temp = ListNode()  
        temp.val = val
        temp.next = node  
        node = temp 
        return node  
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        li = []
        for l in lists:
            if l is None:
                continue
            temp = []
            k = l
            while(k.next is not None):
                temp.append(k.val)
                k = k.next
            temp.append(k.val)
            li.extend(temp)
        s = sorted(li)
        ans = None
        for i in range(len(s)-1,-1,-1):
            ans = self.insert(ans, s[i])
        return ans
            
                        