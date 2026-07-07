class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size_arr=len(nums)
        result=[]
        set_result=set()
        for index_target in range(size_arr):
            if index_target > 0 and nums[index_target] == nums[index_target - 1]:
                continue

            target=nums[index_target]
            l=index_target+1
            r=size_arr-1

            while l<r:
                curr=nums[l]+nums[r]
                if curr==-target:
                    unique_triple=tuple(sorted([target, nums[l], nums[r]]))
                    if not unique_triple in set_result:
                        set_result.add(unique_triple)
                        result.append([target, nums[l], nums[r]])

                    l += 1
                    r -= 1
                elif curr>-target:
                    r -= 1
                else:
                    l += 1
            
        return result 