class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res ={}

        for i in strs:
            ges = "".join(sorted(i))

            if ges not in res:
                res[ges] = []

            
            res[ges].append(i)

        
        return list(res.values())

        