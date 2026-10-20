class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        m = []

        for i in range(len(nums)):
            if nums[i] != 0:
                m.append(nums[i])

        for j in range(len(nums)):
            if nums[j] == 0:
                m.append(nums[j])

        for k in range(len(nums)):
            nums[k] = m[k]