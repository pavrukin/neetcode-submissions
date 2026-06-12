class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # dp[i] will store all unique combinations that add up to 'i'
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]] # Base case: there is one way to make 0 (an empty combo)
        
        for num in nums:
            for i in range(num, target + 1):
                # For every combination that makes (i - num), 
                # we can add 'num' to it to make 'i'
                for combo in dp[i - num]:
                    dp[i].append(combo + [num])
                    
        return dp[target]