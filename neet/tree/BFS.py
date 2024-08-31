# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List, Optional
#neet code bfs
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=collections.deque()
        q.append(root)
        while q:
            a=[]
            l=len(q)
            for _ in range(l):
                node=q.popleft()
                if node:
                    a.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if a:
                ans.append(a)
        return ans

#my BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node,idx,lvl):
            if not node:
                return lvl
            if len(lvl)==idx:
                lvl.append([])
            lvl[idx].append(node.val)
            if node.left:
                dfs(node.left,idx+1,lvl)
            if node.right:
                dfs(node.right,idx+1,lvl)
            return lvl    
        return dfs(root,0,[])
            