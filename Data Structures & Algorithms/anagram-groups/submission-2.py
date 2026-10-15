class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c)-ord("a")] +=1
            if tuple(chars) in anagrams:
                anagrams[tuple(chars)].append(s)
            else:
                anagrams.update({tuple(chars):[s]})
        return list(anagrams.values())