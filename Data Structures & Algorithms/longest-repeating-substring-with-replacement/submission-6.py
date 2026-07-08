class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = [0] * 26
        l = 0
        max_freq = 0
    
        for r, char in enumerate(s):
            # Map 'A'-'Z' to index 0-25
            # ASCII / Unicode Number of A is 65
            r_idx = ord(char) - 65 
            counts[r_idx] += 1
        
            if counts[r_idx] > max_freq:
                max_freq = counts[r_idx]
            
        # Non-shrinking window check
            if (r - l + 1) - max_freq > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            
        return len(s) - l