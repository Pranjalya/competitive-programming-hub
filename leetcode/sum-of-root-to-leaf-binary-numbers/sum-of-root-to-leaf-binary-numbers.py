# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def getPath(self, current, parent):
        stack = []
        
        # Iterate through the nodes and push the values on stack leaf-to-root wise
        while(current):
            stack.append(current.val)
            current = parent[current]
            
        # Since we need the binary value to be in root-to-leaf, get the decimal of the reverse string
        return int(''.join(list(map(str, stack[::-1]))), 2)
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        if root==None:
            return
        
        # Store the progressions in a stack
        stack = []
        stack.append(root)
        
        # Dictionary to store parents of a node
        parent = {}
        parent[root]=None
        
        # Pop all items one by one.
        # 1. Append its right child and set its parent pointer  
        # 2. Append its left child and set its parent pointer  
        # Right child is appended first so that left child is processed first 
        while(len(stack)!=0):
            current = stack[-1]
            stack.pop(-1)
            
            # Get the path if no child nodes
            if (not current.left and not current.right):
                ans += self.getPath(current, parent)
            
            # Traverse right node if available
            if current.right:
                stack.append(current.right)
                parent[current.right] = current
            
             # Traverse left node if available
            if current.left:
                stack.append(current.left)
                parent[current.left] = current
        
        return ans