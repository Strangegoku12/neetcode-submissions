from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0

        while j != len(numbers):
            complement = target - numbers[j]

            for i in range(len(numbers)):
                if i != j and numbers[i] == complement:
                    return [j,i]

            j += 1

        return []