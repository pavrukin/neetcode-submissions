class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        self.set_nums=set(nums)
        lenconsec=[]
        
        def isitemplusone(item,count):
            if item+1 in self.set_nums:        
                count+=1
                self.set_nums.remove(item+1)
                isitemplusone(item+1,count)
            else:
                self.maxcount_right=count
                return 

        def isitemminusone(item,count):
            if item-1 in self.set_nums:        
                count+=1
                self.set_nums.remove(item-1)
                isitemminusone(item-1,count)
            else:
                self.maxcount_left=count
                return

            
        while self.set_nums:
            self.maxcount_right=0
            self.maxcount_left=0
            item=self.set_nums.pop()
            isitemplusone(item,1)
            isitemminusone(item,1)
            lenconsec.append(self.maxcount_left+self.maxcount_right-1)
        
        return max(lenconsec) 