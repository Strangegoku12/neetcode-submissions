class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts = {}
        countt = {}

        # Count characters in s
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        # Count characters in t
        for j in range(len(t)):
            if t[j] in countt:
                countt[t[j]] += 1
            else:
                countt[t[j]] = 1

        return counts == countt

