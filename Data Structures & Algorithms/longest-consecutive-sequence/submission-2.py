class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        longest=0
        for n in nums:
            sequence=1
            if n not in distinct:
                continue
            i=1
            while n+i in distinct:
                sequence +=1
                distinct.remove(n+i)
                i+=1
            j=1
            while n-j in distinct:
                sequence +=1
                distinct.remove(n-j)
                j+=1
            
            longest = max(longest,sequence)
        return longest

        