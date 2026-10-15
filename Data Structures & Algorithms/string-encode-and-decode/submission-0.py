class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            message += str(len(s))+"#"+s
        return message
    def decode(self, s: str) -> List[str]:
        message = []
        i=0
        while i < len(s):
            print(i)
            chars = ""
            while s[i] != "#":
                chars += s[i]
                i+=1
            n=int(chars)
            word = s[i+1:i+n+1]
            i+=n+1
            print(word)
            message.append(word)
        return message
