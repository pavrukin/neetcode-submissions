class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_lett={}
        for word in strs:
            # we create the 26 empty (for all low letters) array
            count=[0]*26
            for char in word:
                # add for each word it's pattern
                count[ord(char)-ord('a')]+=1
            # create the key with the complex structure of the tuple
            key=tuple(count)
            # add 
            dict_lett.setdefault(key,[]).append(word)
        
        return list(dict_lett.values())

