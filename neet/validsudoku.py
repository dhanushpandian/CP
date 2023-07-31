class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            d = []
            for c in r:
                if c!=".":
                    if c in d:
                        return False
                    d.append(c)
        for c in range(9):
            d = []
            for r in range(9):
                n = board[r][c]
                if n!=".":
                    if n in d:
                        return False
                    d.append(n)
        for r in range(3):
            for c in range(3):
                d = []
                for rr in range(r * 3, r * 3 + 3):
                    for cc in range(c * 3, c * 3 + 3):
                        n = board[rr][cc]
                        if n!=".":
                            if n in d:
                                return False
                            d.append(n)
        return True




