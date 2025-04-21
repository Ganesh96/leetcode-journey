class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while(left<right):
            h = min(height[left],height[right])
            area = max(area, (right-left)*h)
            if(height[left]<=height[right]):
                left+=1
            else: #elif(height[left]>height[right]):
                right-=1
        return area