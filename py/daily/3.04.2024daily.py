from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        i=0
        l=len(word)
        seen=set()

        def dfs(r,c,i):
            if i==l:
                return True
            if r>=row or c>=col or r<0 or c<0 or board[r][c]!=word[i] or (r,c) in seen:
                return False
            seen.add((r,c))
            result=(dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1))
            seen.remove((r,c))
            return result

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): 
                    return True
        return False