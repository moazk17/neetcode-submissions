class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_freq[s[i]] += 1
            t_freq[t[i]] += 1
        return s_freq==t_freq