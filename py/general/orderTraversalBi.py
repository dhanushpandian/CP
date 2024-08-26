from  typing import List, Optional
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def fun(root):
            if not root : return 
            ans.append(root.val)
            fun(root.left)
            fun(root.right)
            return ans
        return fun(root)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def fun(root):
            if not root :
                return []
            fun(root.left)
            fun(root.right)
            ans.append(root.val)
            return ans
        return fun(root)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def fun(root):
            if not root:
                return []
            fun(root.left)
            ans.append(root.val)
            fun(root.right)
            return ans
        return fun(root)


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        ans=[]
        def recursion(root):
            for i in root.children:
                recursion(i)
            ans.append(root.val)
        
        recursion(root)
        return ans