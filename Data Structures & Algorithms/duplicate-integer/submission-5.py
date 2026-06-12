class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates=set()
        i=0
        while i<len(nums):
            duplicates.add(nums[i])
            print("i",i)
            if len(duplicates)==i:
                return True
            i+=1    
        return False