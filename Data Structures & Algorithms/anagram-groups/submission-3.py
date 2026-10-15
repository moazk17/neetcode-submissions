class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord("a")] +=1
            chars = tuple(key)
            if chars in anagrams:
                anagrams[chars].append(s)
            else:
                anagrams.update({chars:[s]})
        return list(anagrams.values())