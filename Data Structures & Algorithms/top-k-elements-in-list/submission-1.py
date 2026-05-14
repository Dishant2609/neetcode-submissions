class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        
        arr = []

        for key,value in res.items():
            arr.append([value,key])

        arr.sort()

        bes = []

        while len(bes) < k:
            bes.append(arr.pop()[1])
        return bes
        
        
