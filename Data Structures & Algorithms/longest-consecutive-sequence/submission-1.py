class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        self.set_nums=set(nums)
        self.maxcount=0
        lenconsec=[]
        
        def isitemplusone(item,count):
            #print("item",item)
            #print("count",count)
            if item+1 in self.set_nums:        
                count+=1
                isitemplusone(item+1,count)
            else:
                self.maxcount=count
                return 

            
        for item in nums:
            self.maxcount=0
            isitemplusone(item,1)
            #print("value",self.maxcount)
            lenconsec.append(self.maxcount)
            #print(lenconsec)  
        
        return max(lenconsec)            