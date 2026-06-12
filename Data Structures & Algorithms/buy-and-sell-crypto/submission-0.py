from itertools import accumulate
import numpy as np
class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        cum_min=list(accumulate(prices,min))
        diff=np.max(np.array(prices)-np.array(cum_min))
        print("diff",diff)
        if diff>0: return int(diff)
        else: return 0

        