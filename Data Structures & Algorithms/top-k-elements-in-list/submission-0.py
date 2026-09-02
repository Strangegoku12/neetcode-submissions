class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        l = []

        # Count frequency manually
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        # Now find top k frequent numbers (simple)
        for _ in range(k):
            max_num = max(m, key=m.get)  # number with highest frequency
            l.append(max_num)
            m.pop(max_num)  # remove it so next max can be found

        return l
