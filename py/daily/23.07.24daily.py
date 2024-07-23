
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1          
        a=[[d[i],i] for i in d]
        a.sort() 
        d2={}
        for i in a:
            if i[0] not in d2:
                d2[i[0]]=[]
            d2[i[0]].append(i[1])
        print(d2)
        ans=[]        # for i in :
        #     for j in range(i[0]):
        #         ans.append(i[1])

        return  ans
        
