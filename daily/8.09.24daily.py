# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        def dfs(head,root):
            if not head :
                return True
            if not root:
                return False
            return root.val==head.val and (dfs(head.next,root.left) or dfs(head.next,root.right))
            # else:
            #     return dfs(head,root.right) or dfs(head,root.right)
        return dfs(head, root) or dfs(head, root.left) or dfs(head, root.right)
    
##AI CODE:
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        
        if not root: 
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)