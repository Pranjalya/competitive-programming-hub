# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root): 
        current = root  
        stack = [] 
        l = []
        while True: 
            if current is not None:  
                stack.append(current)
                current = current.left  
            elif(stack): 
                current = stack.pop() 
                l.append(current.val)
                current = current.right  
            else:
                break
        return l
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1 = self.inOrderTraversal(root1)
        t2 = self.inOrderTraversal(root2)
        return sorted(t1+t2)
            