class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_elements=0
        for i in range(len(nums)):
            j=0     

            min_element=nums[i]
            max_element=nums[i]
            while (i+j)<len(nums):
                min_element=min(min_element,nums[i+j])
                max_element=max(max_element,nums[i+j]) 
                print("i+j",i,j)
                diff_elements=abs(max_element-min_element)
                print("diff_elements",diff_elements)
                
                if diff_elements>limit:
                  break
                
                current_length = j + 1
                max_elements = max(max_elements, current_length)
                j+=1
            

        return max_elements