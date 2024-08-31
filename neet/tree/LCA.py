#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return
            if root.val >= p.val and root.val <= q.val or root.val <= p.val and root.val >= q.val:
                return root
            elif root.val > p.val and root.val > q.val:
                return dfs(root.left)
            else:
                return dfs(root.right)
        return dfs(root)
    

    def LCA(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur=root
        while cur:
            if p.val<cur.val and q.val<cur.val:
                cur=cur.left
            elif p.val>cur.val and q.val>cur.val:
                cur=cur.right
            else:
                return cur
        return None