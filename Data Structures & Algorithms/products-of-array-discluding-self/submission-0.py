class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply all without 0
        # create set of indexes where the value is 0
        zero_count=0
        multy=1
        result=[]
        for i in range(len(nums)):
            if nums[i]==0: zero_count+=1
            else: multy*=nums[i]

         

        for i in range(len(nums)):
            if nums[i]==0:
                if zero_count>1:
                    result.append(0)
                else: result.append(multy)
            else:
                if zero_count>0:
                    result.append(0)
                else: result.append(int(multy/nums[i]))
        
        return result


