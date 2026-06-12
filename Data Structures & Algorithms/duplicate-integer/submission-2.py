class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates=set()
        for i in range(len(nums)):
            duplicates.add(nums[i])
            if len(duplicates)<(i+1):
                return True
            
        return False