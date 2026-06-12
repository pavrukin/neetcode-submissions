class Solution:
    def isValid(self, s: str) -> bool:
        setcounter=[]
        lr_dict={")":"(","]":"[","}":"{"}
        left=lr_dict.values()
        for char in s:
            if char in left:
                setcounter.append(char)
            if char in lr_dict:
                if setcounter:
                    if lr_dict[char]==setcounter[-1]:
                        setcounter.pop()
                    else:
                        return False
                else:
                    return False
        return not setcounter

        