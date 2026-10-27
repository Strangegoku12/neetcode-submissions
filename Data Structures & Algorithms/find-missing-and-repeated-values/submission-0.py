
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums1 = []
        k = []

        for i in range(len(grid)):
            for j in range(len(grid)):
                nums1.append(grid[i][j])

        for j in range(1, len(nums1) + 1):
            if j not in nums1:
                k.append(j)
                break

        for j in nums1:
            if nums1.count(j) > 1:
                k.insert(0, j)
                break

        return k
