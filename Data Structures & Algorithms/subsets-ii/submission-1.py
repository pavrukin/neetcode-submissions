from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        # Count frequencies: e.g., [1, 2, 1] becomes {1: 2, 2: 1}
        counts = Counter(nums)
        
        for num, count in counts.items():
            # Dynamically multiply existing subsets by the frequency of the new number
            # If '1' appears twice, we create copies adding [1] and copies adding [1, 1]
            new_subsets = []

            # 1. Loop through every subset we have generated so far
            for curr in results:
                # 2. Loop through how many times we want to repeat the duplicate number
                for i in range(1, count + 1):
                # 3. Create the new combo (e.g., [] + [1] * 2 becomes [1, 1])
                    new_combo = curr + [num] * i
                    new_subsets.append(new_combo)

            # 4. Merge all the newly generated subsets back into our main results list
            results.extend(new_subsets)
            
        return results