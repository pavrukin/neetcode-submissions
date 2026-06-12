class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indic={}
        for index,num in enumerate(nums):
            diff=target-num
            if diff in indic: 
                return [indic[diff],index]         
            indic[num]=index
        
        