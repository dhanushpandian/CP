class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arr=[[min(i)] for i in arrays]
        max_arr=[[max(i)] for i in arrays]
        c=0
        for i in range(len(arrays)):
            min_arr[i].append(i)
            max_arr[i].append(i)
            c+=1
        min_arr.sort()
        max_arr.sort(reverse=True)
        i,j=0,0
        if min_arr[i][1]!=max_arr[j][1]:
            return max(abs(min_arr[i][0]-max_arr[j][0]),abs(min_arr[j][0]-max_arr[i][0]))
        else:
            if min_arr[i+1][0]-max_arr[j][0] > max_arr[i+1][0]-min_arr[j][0]:
                i+=1
            else:
                j+=1
            return max(abs(min_arr[i][0]-max_arr[j][0]),abs(min_arr[j][0]-max_arr[i][0]))



 
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arr=sorted([[min(arrays[i]),i] for i in range(len(arrays))])
        max_arr=sorted([[max(arrays[i]),i] for i in range(len(arrays))],reverse=True)
        i,j=0,0
        if min_arr[i][1]!=max_arr[j][1]:
            return max(abs(min_arr[i][0]-max_arr[j][0]),abs(min_arr[j][0]-max_arr[i][0]))
        else:
            if min_arr[i+1][0]-max_arr[j][0] > max_arr[i+1][0]-min_arr[j][0]:
                i+=1
            else:
                j+=1
            return max(abs(min_arr[i][0]-max_arr[j][0]),abs(min_arr[j][0]-max_arr[i][0]))
            