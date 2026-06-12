class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results=[]

        def backtracking(remain: int, combo: List[int], start_index: int):

            if remain==0:
                results.append(list(combo))
                return
            
            for i in range(start_index, len(candidates)):
                if candidates[i]>remain:
                    break
                
                if i>start_index and candidates[i]==candidates[i-1]:
                    continue

                combo.append(candidates[i])

                backtracking(remain-candidates[i],combo,i+1)
                
                combo.pop()
        
        backtracking(target, [], 0)
        return results
    

