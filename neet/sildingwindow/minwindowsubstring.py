class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Initialize a dictionary to store the character frequencies in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # Initialize pointers and counters
        left = 0
        min_len = float('inf')
        min_window_start = 0
        chars_to_match = len(t_count)
        matched_chars = 0
        
        for right in range(len(s)):
            # Update the character count for the right pointer
            if s[right] in t_count:
                t_count[s[right]] -= 1
                if t_count[s[right]] == 0:
                    matched_chars += 1

            # While all characters from t are matched, update the left pointer
            while matched_chars == chars_to_match:
                if right - left < min_len:
                    min_len = right - left
                    min_window_start = left

                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        matched_chars -= 1

                left += 1

        if min_len == float('inf'):
            return ""
        return s[min_window_start:min_window_start + min_len + 1]
