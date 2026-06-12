class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            print( "nums[mid]",nums[mid])
            print( "nums[left]",nums[left])
            print( "nums[right]",nums[right])
            if nums[mid]== nums[right]:
                return nums[right]
            if nums[mid] > nums[right]:
                left=mid+1
            else: right=mid

        return nums[mid]
        