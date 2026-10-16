class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        longest=0
        for n in distinct:
            if n-1 not in distinct:
                sequence=1
                while n+sequence in distinct:
                    sequence+=1
                longest=max(longest,sequence)

        return longest

        