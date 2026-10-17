class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                j=stack[-1][0]
                res[j] = i-j
                stack.pop()
            stack.append([i,t])
        return res

        