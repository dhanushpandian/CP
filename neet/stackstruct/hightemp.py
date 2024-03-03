#my code optimized by gpt
class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  
        for i in range(n - 2, -1, -1):
            j = i + 1  
            while j < n:
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
                elif answer[j] == 0:
                    break
                else:
                    j += answer[j]  
            
        return answer

#neet code solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  
        stack = []  
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)  
        
        return answer
