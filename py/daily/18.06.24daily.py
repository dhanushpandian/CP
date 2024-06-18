#my 1st attempt approach
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d={difficulty[i]: profit[i] for i in range(len(profit))}
        ans=0
        a=sorted(difficulty)
        for i in worker:
            p=0
            for j in a:
                if j <= i:
                    p=max(p,d[j])
                else:
                    break
            ans+=p

        return ans

#solution from leetcode
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
            sorted_worker=sorted(worker)
            jobs=zip(difficulty,profit)
            sorted_jobs=sorted(jobs)
            n=len(sorted_jobs)
            best_profit=0
            total_best_profit=0
            i=0
            for skill in sorted_worker:
                while i<n and skill>=sorted_jobs[i][0]:
                    best_profit=max(best_profit, sorted_jobs[i][1])
                    i+=1
                total_best_profit+=best_profit
            return total_best_profit        