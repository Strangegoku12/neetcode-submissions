class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        k = []

        def subset1(index, ds):
            if index >= len(nums):
                k.append(ds.copy())
                return

            # Pick
            ds.append(nums[index])
            subset1(index + 1, ds)

            # Not Pick
            ds.pop()
            subset1(index + 1, ds)

        subset1(0, [])
        return k