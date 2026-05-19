class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                    top = stack.pop()
                    days = i - top[1]
                    res[top[1]] = days
            
            stack.append((temperatures[i], i))

        return res
