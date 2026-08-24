class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        left=0
        square_max=0
        while right>left:
            a=right-left
            if heights[right]>heights[left]:
                b=heights[left]
                shift_left=True
            else:
                b=heights[right]
                shift_left=False
            square=a*b
            if square>square_max: square_max=square
            if shift_left==True:
                left+=1 
            else:
                right-=1
        return square_max

