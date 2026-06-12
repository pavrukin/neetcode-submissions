class Solution:
    def isValid(self, s: str) -> bool:
        setcounter=[]
        lr_dict={")":"(","]":"[","}":"{"}
        right=lr_dict.keys()
        left=lr_dict.values()
        for char in s:
            if char in left:
                setcounter.append(char)
            if char in right:
                if setcounter:
                    if lr_dict[char]==setcounter[-1]:
                        setcounter.pop()
                    else:
                        return False
                else:
                    return False
        return not setcounter

        