class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sk=s.strip()
        t=""
        for i in range(len(sk) - 1, -1, -1):
            if sk[i] != ' ':
                t+=sk[i]
            else:
                break
        m=len(t)
        return m