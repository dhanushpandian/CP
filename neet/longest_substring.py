class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store unique characters in the current substring
        max_length = 0    # To store the length of the longest substring
        left = 0          # Left pointer of the sliding window
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
