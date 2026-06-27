class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Convert to a set for O(1) lookups
        num_set = set(nums)
        max_streak = 0
        
        for num in num_set:
            # Check if 'num' is the START of a consecutive sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Expand the sequence upward
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Keep track of the longest one found
                max_streak = max(max_streak, current_streak)
                
        return max_streak