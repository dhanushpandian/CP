class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s=sentence[0]
        prev=None
        flag=True
        i=0
        while i < len(sentence):
            if sentence[i] != " ":
                prev=sentence[i]
                i+=1
            else:
                i+=1
                if sentence[i] != prev:
                    flag=False
                    break
        return flag and s == sentence[-1]
