class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k=1
        high_k=max(piles)
        result = high_k

        while low_k<=high_k:
            k=(low_k+high_k)//2
            total_h=0
            for pile in piles:
                h_pile=pile//k
                if pile%k: h_pile+=1
                total_h+=h_pile

            if total_h <= h:
                result=k 
                high_k=k-1
            elif total_h > h: 
                low_k=k+1

        return result
        
