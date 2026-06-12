class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums=sorted(candidates)
        results=[]

        def backtracking(remain: int, combo: List[int], start_index: int):

            if remain==0:
                results.append(list(combo))
                return
            
            for i in range(start_index, len(nums)):
                if nums[i]>remain:
                    break
                
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                    
                combo.append(nums[i])

                backtracking(remain-nums[i],combo,i+1)
                
                combo.pop()
        
        backtracking(target, [], 0)
        return results
    

