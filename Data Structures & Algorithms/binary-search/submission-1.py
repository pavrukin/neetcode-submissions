class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right=len(nums)-1
        left=0
        
        while left<=right:
            position=(left+right)//2
            if nums[position]==target: return position
            elif nums[position]>target: right=position-1
            else: left=position+1
        return -1

