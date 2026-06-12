class Solution:
   # without backtracking
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # dp[i] will store all unique combinations that add up to 'i'
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]] # Base case: there is one way to make 0 (an empty combo)
        
        for num in nums:
         #   print("enter num", num)
            for i in range(num, target + 1):
               # print("enter i", i)
                # For every combination that makes (i - num), 
                # we can add 'num' to it to make 'i'
               # print(f"dp[{i} - {num}]")
                for combo in dp[i - num]:
                   # print("enter combo", combo)
                    dp[i].append(combo + [num])
                   # print(f"dp[{i}].append(combo{combo} + [{num}])")
                   # print(f"dp[{i}]=",dp[i])
                    
        return dp[target]