class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i]>temperatures[stack[-1]]:
                while(stack and temperatures[i]>temperatures[stack[-1]]):
                    top = stack.pop()
                    ans[top]=i-top
            stack.append(i)
        while stack:
            top = stack.pop()
            ans[top]=0
        return ans