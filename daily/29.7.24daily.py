#Naive Brute Force Solution
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans=0
        n=len(rating)
        for i in range(n-2):
            for j in  range(i,n-1):
                for k in range(j,n):
                    if (rating[i] < rating[j] and rating[j] < rating[k]) or (rating[i] > rating[j] and rating[j] > rating[k]):
                        ans+=1
        return ans
    
#Optimized Solution
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans=0
        n=len(rating)
        for i in range(n):
            left_less=left_great=right_less=right_great=0
            for j in range(i):
                if rating[j]<rating[i]:
                    left_less+=1
                else:
                    left_great+=1
            for j in range(i+1,n):
                if rating[j]<rating[i]:
                    right_less+=1
                else:
                    right_great+=1
            ans+=left_less*right_great+left_great*right_less
        return ans