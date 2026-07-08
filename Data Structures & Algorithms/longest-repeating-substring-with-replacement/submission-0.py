class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        if k>len(s) and k<26: return len(s)

        dict_letter={}
        l=0
        r=1
        dict_letter[s[0]]=1
        max_len=1
        max_freq=1

        while r<len(s):
            rchar=s[r]
            dict_letter[rchar]=dict_letter.get(rchar,0)+1
            max_freq = max(max_freq, dict_letter[rchar])

            while (r-l+1) - max_freq > k:
                dict_letter[s[l]]-=1
                if  dict_letter[s[l]] == 0 :
                    del dict_letter[s[l]]
                l+=1
            max_len=max(max_len, r-l+1)
            r+=1
        
        return max_len
            
                
                

