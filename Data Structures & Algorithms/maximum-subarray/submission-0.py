class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        totalsum=0

        for n in nums:
            if totalsum < 0:
                totalsum=0
            totalsum+=n
            maxi=max(totalsum,maxi)
        return maxi
        