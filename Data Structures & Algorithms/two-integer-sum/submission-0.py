class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indic={}
        for index,num in enumerate(nums):
            if (target-num) in indic: 
                return [indic[target-num],index]         
            indic[num]=index
        
        