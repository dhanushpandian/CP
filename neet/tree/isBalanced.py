class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root) -> int:
            if not root:
                return 0
            
            left_height = height(root.left)
            if left_height == -1:
                return -1
            
            right_height = height(root.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return height(root) != -1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root)->int:
            if not root:
                return 0
            else:
                return 1+ max(height(root.left),height(root.right))
        if not root:
            return True
        l=height(root.left)
        r=height(root.right)
        if not self.isBalanced(root.right):
            return False
        if not self.isBalanced(root.left):
            return False
        return True if abs(l-r) <=1  else False and self.isBalanced(root.left.left) and self.isBalanced(root.right.right)