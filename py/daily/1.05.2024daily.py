class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        indx=0
        for i in range(len(word)):
            if word[i] == ch:
                indx=i
                break
        ans=[]
        for i in range(len(word)):
            if i<=indx:
                ans.insert(0,word[i])
            else:
                ans.append(word[i])
        return "".join(ans)

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=word.find(ch)
        return word[:x+1][::-1]+word[x+1:]

