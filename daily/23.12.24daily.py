# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swaps(arr): 
            n = len(arr) 
            original = list(arr) 
            index_map = {v: i for i, v in enumerate(arr)} 
            sorted_arr = sorted(arr) 
            swaps_count = 0 
            for i in range(n): 
                if arr[i] != sorted_arr[i]: 
                    swaps_count += 1 
                    to_swap_idx = index_map[sorted_arr[i]] # Swap elements 
                    arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i] # Update index map 
                    index_map[arr[to_swap_idx]] = to_swap_idx 
                    index_map[arr[i]] = i 
                    
            return swaps_count


        if not root:
            return 0

        a = []
        a.append(root)
        c = 0
        d = {c: [root.val]}

        while a:
            level_size = len(a)
            c += 1
            d[c] = []
            for _ in range(level_size):
                n = a.pop(0)
                if n.left:
                    d[c].append(n.left.val)
                    a.append(n.left)
                if n.right:
                    d[c].append(n.right.val)
                    a.append(n.right)

        print(d)
        ans = 0
        for i in d.values():
            ans+=swaps(i)
        

        return ans

