class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def fun(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val==q.val and fun(p.left,q.left) and fun(p.right,q.right)
        return fun(p,q)