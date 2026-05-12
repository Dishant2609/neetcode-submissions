class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        t = set(nums)
        longest = 0


        for i in nums:
            if (i-1) not in t:
                length = 0
                while (i + length) in t:
                    length += 1

                longest = max(length, longest)

        return longest          
