class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        l1=len(v1)
        l2=len(v2)
        i,j=0,0
        while (i<l1 or j<l2):
            n1= int(v1[i]) if i < l1 else 0
            n2= int(v2[j]) if j < l2 else 0
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            # if not v1[i]:
            #     return -1
            # if not v2[i]:
            #     return 1
            # if int(v1[i]) > int(v2[j]):
            #     return 1
            # if int(v1[i]) < int(v2[j]):
            #     return -1
            i+=1
            j+=1
        return 0
