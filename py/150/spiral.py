class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ans = []
        while t <= b and l <= r:
            # Traverse top row from left to right
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            t += 1
            # Traverse rightmost column from top to bottom
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            # Traverse bottom row from right to left
            if t <= b:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[b][i])
                b -= 1
            # Traverse leftmost column from bottom to top
            if l <= r:
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])
                l += 1
        return ans
