class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans={}
        for i in nums:
            s=list(str(i))
            #print(s)
            a=[]
            for j in s:
                a.append(mapping[int(j)])
            digit="".join(map(str,a))
            ans[i]=int(digit)
        #print(ans)
        return sorted(nums, key = lambda x: (ans[x] , nums.index(x) ))
    

from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)
        
        # Create a list of tuples (mapped_value, original_index, original_value)
        mapped_nums = [(get_mapped_value(num), i, num) for i, num in enumerate(nums)]
        
        # Sort based on the mapped value and original index to preserve order for equal mapped values
        mapped_nums.sort()
        
        # Extract the original numbers from the sorted tuples
        return [num for _, _, num in mapped_nums]

# Example usage
solution = Solution()
mapping = [9, 3, 1, 5, 4, 0, 7, 2, 6, 8]
nums = [621261067, 45659166, 836957040, 982712940, 169622778, 801076686, 476924985, 218282960, 467631198, 628221122, 730499638, 663509156, 843535562, 245971464, 52814505, 330403696, 877680024, 560201434, 399239107]
print(solution.sortJumbled(mapping, nums))
