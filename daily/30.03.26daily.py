class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        d1_odd={}
        d1_eve={}
        d2_odd={}
        d2_eve={}
        for i in range(len(s1)):
            if i%2 ==0:
                if s1[i] in d1_eve:
                    d1_eve[s1[i]]+=1
                else:
                    d1_eve[s1[i]]=1
                if s2[i] in d2_eve:
                    d2_eve[s2[i]]+=1
                else:
                    d2_eve[s2[i]]=1
            else:
                if s1[i] in d1_odd:
                    d1_odd[s1[i]]+=1
                else:
                    d1_odd[s1[i]]=1
                if s2[i] in d2_odd:
                    d2_odd[s2[i]]+=1
                else:
                    d2_odd[s2[i]]=1
        # print(d1_odd,d1_eve)
        # print(d2_odd,d2_eve)

        return d1_eve==d2_eve and d1_odd==d2_odd
