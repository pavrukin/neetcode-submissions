class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        left=0
        square_max=0
        while right>left:
            a=right-left
            if heights[right]>heights[left]:
                b=heights[left]
                shift_next="left"
            else:
                b=heights[right]
                shift_next="right"
            square=a*b
            if square>square_max: square_max=square
            if shift_next=="right": 
                right-=1
            else:
                left+=1
        return square_max

