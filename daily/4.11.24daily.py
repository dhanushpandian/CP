class Solution:
    def compressedString(self, word: str) -> str:
        if not word: return ""
        c = []
        prev = word[0]
        n = 1
        for i in range(1, len(word)):
            if word[i] != prev:
                c.append([prev, n])
                prev = word[i]
                n = 1
            else:
                n += 1
        c.append((prev, n)) 
        comp = ""
        #print(c)
        for char, count in c:
            while count > 9:
                comp += str(9) + char 
                count-=9
            comp += str(count) + char
        return comp
