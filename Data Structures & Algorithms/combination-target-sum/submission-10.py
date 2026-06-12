class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = [x for x in sorted(set(nums)) if x <= target]
        
        result=[]

        def backtracking(remain: int, combo: List[int], start_index: int):
            # case one we hit the target
            if remain==0:
                # by using list(combo) we take the copy of current combination
                result.append(list(combo))
                return
            
            if remain<0:
                # we overscore the targer
                return
            
            # other possibilities
            for i in range(start_index, len(nums)):
                #if the firsr element with start_index is larger than remain
                # no reason to continue
                if nums[i]>remain:
                    break
                
                # 1 add combo to the current path
                combo.append(nums[i])

                # 2 explore i as the start index 
                backtracking(remain-nums[i], combo, i)

                # 3 unchoose combo for the next try (backtracking) 
                #   before the next i in the iteration
                combo.pop()

        backtracking(target, [], 0)
        return result

            
 