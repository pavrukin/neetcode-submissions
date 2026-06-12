class Solution:
    def isHappy(self, n: int) -> bool:
        cyclical_set=set()
        while n not in cyclical_set:
            cyclical_set.add(n)
            a=n//100
            print("a",a)
            b=(n-100*a)//10
            print("b",b)
            c=n-100*a-10*b
            print("c",c)
            n=a*a+b*b+c*c
            print ("n",n)
            print ("cyclical_set",cyclical_set)
            if n==1: return True
        return False
        