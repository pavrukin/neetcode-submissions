class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results=[]
        #creating copy of sorted values in nums
        nums.sort()
        length_array=len(nums)
        
        def backtracking(current_combo, curr_index):
            # check if something left
            results.append(list(current_combo))
                #if exists skip for the next iteration    
            for i in range(curr_index,length_array):
                if i > curr_index and nums[i]==nums[i-1]:
                    continue
                current_combo.append(nums[i])
                backtracking(current_combo,i+1)
                #backtrack remove the number
                current_combo.pop()


            # check through all the element left
        
        backtracking([],0)
        return results
            
            
    
