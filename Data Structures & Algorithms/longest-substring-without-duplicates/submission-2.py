from collections import deque 
import numpy as np
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        if len(s)==2:
            if s[0]!=s[1]:
                return 2
            else: 
                return 1
        
        #creating pointers and hash set 
        dict_letter={}
        l=0
        dict_letter[s[l]]=1
        r=1
        max_length=1
        current_length=1

        while r<len(s):
            rchar=s[r]
            dict_letter[rchar]=dict_letter.get(rchar,0)+1

            while dict_letter[rchar]>1:
                dict_letter[s[l]]-=1
                if dict_letter[s[l]]==0: 
                    del dict_letter[s[l]]
                current_length-=1
                l+=1 
                 
            current_length+=1
            if current_length>max_length:
                max_length=current_length
            r+=1
        return max_length
            


