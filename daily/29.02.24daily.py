
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isEvenOddTree(self, root) -> bool:
        even=True
        q=deque([root])
        while q:
            prev=float("-inf") if even else float("inf")
            l=len(q)
            for _ in range(len(q)):
                node=q.popleft()
                if even:
                    if node.val % 2 == 0 or node.val<=prev:
                        return False
                else: 
                    if node.val%2==1 or node.val>=prev:
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev=node.val
            even=not even
        return True