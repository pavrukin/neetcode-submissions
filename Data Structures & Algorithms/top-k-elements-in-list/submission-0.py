
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictnums={}
        # create dict of element
        for element in nums:
            dictnums[element]=dictnums.get(element,0)+1

        buckets=[[] for _ in range(len(nums)+1)]

        for element, freq in dictnums.items():
            buckets[freq].append(element)

        result=[]

        for i in range(len(nums), 0 ,-1):
            for element in buckets[i]:
                result.append(element)
                if len(result)>=k:
                    return result  
        
