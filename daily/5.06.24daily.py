class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the frequency dictionary for the first word
        cc = {}
        for i in words[0]:
            if i in cc:
                cc[i] += 1
            else:
                cc[i] = 1
        
        # Iterate over the rest of the words
        for word in words[1:]:
            # Initialize a temporary frequency dictionary for the current word
            d = {}
            for char in word:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            
            # Update the common characters frequency dictionary
            for char in cc:
                if char in d:
                    cc[char] = min(cc[char], d[char])
                else:
                    cc[char] = 0
        
        # Collect the common characters based on the updated frequency dictionary
        result = []
        for char, count in cc.items():
            for i in range(count):
                result.append(char)
        
        return result