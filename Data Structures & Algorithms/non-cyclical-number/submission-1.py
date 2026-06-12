class Solution:
    def isHappy(self, n: int) -> bool:
        cyclical_set=set()
        while n not in cyclical_set:
            cyclical_set.add(n)
            a=n//100
            b=(n-100*a)//10
            c=n-100*a-10*b
            n=a*a+b*b+c*c
            if n==1: return True
        return False
        