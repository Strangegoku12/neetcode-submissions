class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumsubarray=0
        maximumsum=nums[0]
        for i in range(len(nums)):
            if maximumsubarray < 0:
                maximumsubarray = 0
            maximumsubarray+=nums[i]
            maximumsum=max(maximumsum,maximumsubarray)
        return maximumsum
        