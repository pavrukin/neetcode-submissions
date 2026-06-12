class Solution:
    def isValid(self, s: str) -> bool:
        setcounter=[]
        lr_dict={")":"(","]":"[","}":"{"}
        for char in s:                
            if char in lr_dict:
                if setcounter:
                    if lr_dict[char]==setcounter[-1]:
                        setcounter.pop()
                    else:
                        return False
                else:
                    return False
            else:        
                setcounter.append(char)
        return not setcounter

        