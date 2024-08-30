


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def fun(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val==q.val and fun(p.left,q.left) and fun(p.right,q.right)
        return fun(p,q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def fun(root,subroot):
            if not subRoot:
                return True
            if not root:
                return False
            if self.isSameTree(root,subroot):
                return True
            return fun(root.right,subRoot) or fun(root.left,subRoot)
        return fun(root,subRoot)