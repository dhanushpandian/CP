class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = 0
        left = [1] * len(ratings)
        right = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(len(ratings)):
            candies += max(left[i], right[i])

        return candies

#optimizedd
class Solution:
    def candy(self, ratings: List[int]) -> int:
        a=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1] :
                a[i] = a[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] :
                a[i] = max( a[i], a[i+1]+1)
        return sum(a)