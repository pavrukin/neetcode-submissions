class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_letter = {}
        l = 0
        max_freq = 0

        for r in range(len(s)):
            dict_letter[s[r]]=dict_letter.get(s[r],0)+1
            max_freq = max(max_freq, dict_letter[s[r]])

            if (r-l+1) - max_freq > k:
                dict_letter[s[l]]-=1
                l+=1
        
        return len(s)-l
            
                
                

