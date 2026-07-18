class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen_permutations=set()
        result=[]

        def check_if_seen(permutation):
            key=tuple(permutation)
            if key in seen_permutations: 
                return True
            seen_permutations.add(key) 
            return False
        
        def backtracking(current_combo, remain_list):
            # if nothing left we check the compbination
            if not remain_list:
                if not check_if_seen(current_combo):
                    result.append(list(current_combo))
                return
            
            for i in range(len(remain_list)):
                value_to_check=remain_list[i]
                current_combo.append(value_to_check)
                remain_choices=remain_list[:i]+remain_list[i+1:]
                backtracking(current_combo,remain_choices)
                current_combo.pop()
            
        backtracking([],nums)

        return result


        
        
        



