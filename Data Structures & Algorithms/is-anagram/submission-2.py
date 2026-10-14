class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new = sorted(s)
        t_new = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s_new[i] != t_new[i]:
                return False
        return True