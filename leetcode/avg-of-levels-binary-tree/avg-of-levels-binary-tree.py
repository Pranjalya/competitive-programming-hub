from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return

        q = deque()
        q.extend([root, None])
        s, l = 0, 0
        ans = []

        while len(q) >= 2:
            current = q.popleft()
            if current is None:
                q.append(None)
                ans.append(s/l)
                s, l = 0, 0
            else:
                if current.left:    q.append(current.left)
                if current.right:   q.append(current.right)
                s += current.val
                l += 1

        if l != 0:
            ans.append(s/l)

        return ans
