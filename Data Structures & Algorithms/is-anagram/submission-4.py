class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_word={}
        for char in s:
            dict_word[char]=dict_word.get(char,0)+1

        for char in t:
            if char not in dict_word:
                return False
            if dict_word.get(char)==1:
                del dict_word[char]
            else: dict_word[char]-=1 

        return not dict_word

        