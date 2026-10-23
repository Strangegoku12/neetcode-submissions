class Solution:
    def sortColors(self, nums: List[int]) -> None:
        k = []

        for i in nums:
            if i == 0:
                k.append(i)

        for j in nums:
            if j == 1:
                k.append(j)

        for l in nums:
            if l == 2:
                k.append(l)

        nums[:] = k