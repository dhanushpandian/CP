class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        s=s.lower()
        print(s)
        while(i<j):
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i]==" ":
                i+=1
                continue
            if s[j]==" ":
                j-=1
                continue
            if s[i]!=s[j]:
                print(s[i])
                return False
            i+=1
            j-=1
        return True

        


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=("".join(i for i in s if i.isalnum())).lower()
        return new==new[::-1]




class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        s=s.lower()
        for i in s:
            if i.isalpha() or i.isnumeric():
                a+=i
        return a==a[::-1]
