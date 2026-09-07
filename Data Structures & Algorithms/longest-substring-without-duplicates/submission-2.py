class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        m = {}
        maxi = 0

        while r < len(s):
            if s[r] not in m:
                m[s[r]] = r
                maxi = max(maxi, r - l + 1)
                r += 1
            else:
                del m[s[l]]
                l += 1

        return maxi