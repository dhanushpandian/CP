class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr=[]
        def combi(a,idx,s):
            if s==target:
                arr.append(a[:])
                return
            for i in range(idx,len(candidates)):
                if s+candidates[i]<=target:
                    a.append(candidates[i])
                    combi(a,i,s+candidates[i])
                    a.pop()
        combi([],0,0)
        return arr