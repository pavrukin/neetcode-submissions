class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        left=0
        square_max=0
        while right>left:
            if heights[right]>heights[left]:
                shift_left=True
                square_max=max(square_max,heights[left]*(right-left))
            else:
                shift_left=False
                square_max=max(square_max,heights[right]*(right-left))
            
            if shift_left==True:
                left+=1 
            else:
                right-=1
        return square_max

