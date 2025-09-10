class Solution:
    def trap(self, height: List[int]) -> int:
        rightm = [0]* len(height)
        leftm = [0]* len(height)
        m = res = 0
        for i in range(len(height)):
            leftm[i] = m
            m = max(m, height[i])
        
        m = 0

        for i in range(len(height)-1,-1,-1):
            rightm[i] = m
            m = max(m, height[i])

        print(leftm)
        print(rightm)
        for i in range(len(height)):
            res += max(min(leftm[i], rightm[i]) - height[i],0)
        return res