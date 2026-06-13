class Solution:
    def isValid(self, s: str) -> bool:

        res = {'}':'{',']':'[',')':'('}

        ges = []

        for i in s:
            if i not in res:
                ges.append(i)
            else:
                if not ges:
                    return False
                else:
                    popped = ges.pop()
                    if popped != res[i]:
                        return False
                
        return not ges