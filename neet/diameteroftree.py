#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root:TreeNode) -> int:
        self.m=0
        def dfs(root):
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            cd=l+r
            self.m=max(self.m,cd)
            return 1+max(r,l)
        dfs(root)
        return self.m
       