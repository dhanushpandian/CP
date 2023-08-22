class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        k = 0
        c = ''
        while k < (len(word1) + len(word2)):
            if k % 2 == 0:
                if i < len(word1):
                    c += word1[i]
                    i += 1
                else:
                    c += word2[j:]
                    break
            else:
                if j < len(word2):
                    c += word2[j]
                    j += 1
                else:
                    c += word1[i:]
                    break
            k += 1
        return c
