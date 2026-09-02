class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        k = sorted(nums)

        count = 1
        maxi = 1

        for i in range(len(k) - 1):

            diff = k[i + 1] - k[i]

            if diff == 1:
                count += 1
                maxi = max(maxi, count)

            elif diff == 0:
                # duplicate hai, ignore karo
                continue

            else:
                # sequence break ho gayi
                count = 1

        return maxi