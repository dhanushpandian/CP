class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        return ('1' * (ones - 1)) + ('0' * (len(s) - ones)) + '1'
    

    def maxOddBinNum(self, s: str) -> str:
        d={}
        for i in s:
            # if i in d:
            #     d[i]+=1
            # else:
            #     d[i]=1
            d[i] = d.get(i, 0) + 1
            # d[i]=d[i]+1 if i in d else 1 
        s=""
        s+="1"*(d.get('1',0)-1)
        s+="0"*(d.get('0',0))
        s+="1"
        # s+="1"*(d['1']-1)
        # s+="0"*(d['0'])
        # s+="1"       
        # print(d)
        return s