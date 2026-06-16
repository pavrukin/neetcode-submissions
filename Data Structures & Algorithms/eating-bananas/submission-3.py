class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #slowest rate to eat bananas
        low_k=1
        # highest rate to eat bananas
        high_k=max(piles)
        #default result to the maximum possible rate
        result = high_k
        
        # we use two pointers unless they meet
        while low_k<=high_k:
            # use binary search for the rate
            k=(low_k+high_k)//2
            total_h=0

            # Calculate total hours needed to eat all piles at speed 'k'
            for pile in piles:
                #celi rounds up to the highest integer celi(4.2)=5
                total_h+=math.ceil(pile/k)
            
            # if banans are eaten within the time limit
            if total_h <= h:
                result=k # Record k as a valid feasible speed
                high_k=k-1 # try to find a smaller valid speed
            # if the rate k is not enoughto finish bananas in h hours
            elif total_h > h: 
                low_k=k+1 # Increase the lower bound

        return result
        
