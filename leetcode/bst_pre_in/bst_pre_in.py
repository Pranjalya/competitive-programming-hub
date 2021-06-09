# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder_idx = 0
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def array_tree(low, high):
            if low > high:
                return None

            nonlocal preorder_idx

            x = TreeNode(preorder[preorder_idx])
            preorder_idx += 1

            mid = inorder_map[x.val]

            x.left = array_tree(low, mid-1)
            x.right = array_tree(mid+1, high)

            return x

        return array_tree(0, len(inorder)-1)

