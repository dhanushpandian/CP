class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        #print(d,[d.values()])
        a=sorted(list(d.keys()),key= lambda x : d[x],reverse=True)
        #print(a)
        dial=0
        ans=0
        for i in a:
            if dial < 8 :
                ans+=d[i]
                dial+=1
            else:
                ans+= d[i] * ((dial//8)+1)
                dial+=1
        return ans